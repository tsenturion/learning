# Импортируем необходимые библиотеки
import numpy as np
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Input, Dense, Conv2D, MaxPool2D, Flatten, Concatenate
from tensorflow.keras.utils import to_categorical
from sklearn.model_selection import StratifiedKFold
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix


# Определяем простую функцию для метрики F1
def f1_metric(y_true, y_pred):
    from keras import backend as K
    true_positives = K.sum(K.round(K.clip(y_true * y_pred, 0, 1)))
    possible_positives = K.sum(K.round(K.clip(y_true, 0, 1)))
    predicted_positives = K.sum(K.round(K.clip(y_pred, 0, 1)))
    precision = true_positives / (predicted_positives + K.epsilon())
    recall = true_positives / (possible_positives + K.epsilon())
    return 2 * ((precision * recall) / (precision + recall + K.epsilon()))


# Генерируем фиктивные данные для демонстрации
data = [np.random.rand(100, 64, 64, 1) for _ in range(3)]  # данные для 3 каналов ЭЭГ
labels = np.random.randint(0, 2, 100)  # бинарные метки

# Настраиваем кросс-валидацию
n_splits = 3
skf = StratifiedKFold(n_splits=n_splits, shuffle=True)
total_acc, total_f1 = 0, 0

for train_idx, test_idx in skf.split(data[0], labels):
    x_train, y_train = [d[train_idx] for d in data], labels[train_idx]
    x_test, y_test = [d[test_idx] for d in data], labels[test_idx]

    y_train_cat = to_categorical(y_train)
    y_test_cat = to_categorical(y_test)

    # Определяем простую модель
    inputs = [Input(shape=(64, 64, 1)) for _ in range(3)]
    convs = [Conv2D(8, 3, activation='relu')(inp) for inp in inputs]
    pools = [MaxPool2D(2)(conv) for conv in convs]
    flats = [Flatten()(pool) for pool in pools]
    combined = Concatenate()(flats)
    output = Dense(2, activation='softmax')(combined)

    model = Model(inputs=inputs, outputs=output)
    model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy', f1_metric])

    # Обучаем модель
    model.fit(x_train, y_train_cat, batch_size=32, epochs=5, validation_split=0.2)

    # Предсказываем и оцениваем модель
    y_pred = model.predict(x_test).argmax(axis=-1)
    acc = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred, average='weighted')
    matrix = confusion_matrix(y_test, y_pred)

    # Выводим результаты
    print(f"Точность на фолде: {acc:.2f}")
    print(f"F1 на фолде: {f1:.2f}")
    print(f"Матрица ошибок на фолде:\n{matrix}")

    total_acc += acc / n_splits
    total_f1 += f1 / n_splits

print(f"Средняя точность модели: {total_acc:.2f}")
print(f"Средний F1 модели: {total_f1:.2f}")
