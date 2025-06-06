# **Текстовки для учителя по уроку "Создание игры-кликера на PyGame"**

---

#### **1. Введение (10 мин)**  
**Учитель:**  
*"Сегодня мы будем создавать свою первую игру на Python с помощью библиотеки PyGame. Это будет простой кликер, где нужно нажимать на карточки. PyGame — это мощный инструмент для 2D-игр, и сегодня мы разберём его основы.  

Обратите внимание на структуру кода:  
- В начале файла идут настройки (размеры окна, цвета).  
- Потом два класса — `Area` (прямоугольник) и `Label` (текст на карточке).  
- В конце — главный цикл игры.  

Давайте запустим код и посмотрим, как это работает!"*  

*(Запускает программу, показывает карточки.)*  

---

#### **2. Работа с графикой (15 мин)**  
**Учитель:**  
*"PyGame рисует всё с помощью прямоугольников (`Rect`). Давайте разберём, как это устроено:  
- `Area` — это просто прямоугольник с цветом.  
- `Label` добавляет текст, но из-за особенностей платформы мы не можем автоматически центрировать его — поэтому используем фиксированные отступы (`TEXT_OFFSET_X/Y`).  

**Практика:**  
Попробуйте изменить цвет карточек. Найдите константу `CARD_COLOR` и поменяйте значения RGB. Например, на `(255, 0, 0)` — это будет красный.  

Вопрос: Как вы думаете, почему для текста нельзя просто взять `get_width()`?"*  

*(Ждёт ответы, объясняет про проблемы рендеринга.)*  

---

#### **3. ООП: Классы `Area` и `Label` (20 мин)**  
**Учитель:**  
*"Теперь разберём, зачем здесь классы:  
- `Area` — это базовая фигура. У неё есть координаты, размер и цвет.  
- `Label` наследует от `Area` и добавляет текст.  

**Вопрос:** Почему `Label` не рисует текст сам, а использует `blit`?  

*(Объясняет: PyGame работает с поверхностями, `blit` — это "накладывание" текста на экран.)*  

**Практика:**  
Давайте добавим ещё одну карточку. Для этого в `create_game_cards()` нужно увеличить `CARDS_COUNT` и проверить, как она появляется."  

*(Ученики пробуют, учитель помогает с синтаксисом.)*  

---

#### **4. Главный игровой цикл (15 мин)**  
**Учитель:**  
*"Сердце игры — это цикл `while running`. В нём происходит:  
1. Обработка событий (например, закрытие окна).  
2. Отрисовка (очистка экрана, рисование карточек).  
3. Контроль FPS (`clock.tick(40)` — 40 кадров в секунду).  

**Практика:**  
Попробуйте изменить FPS на 10. Что происходит? А на 60?  

*(Обсуждают, как FPS влияет на плавность.)*  

---

#### **5. Особенности "Алгоритмики" (10 мин)**  
**Учитель:**  
*"На этой платформе PyGame работает не совсем стандартно:  
- `get_width()` для текста может давать неправильные размеры.  
- Поэтому мы используем "магические" числа `TEXT_OFFSET_X/Y`.  

**Практика:**  
Попробуйте изменить `TEXT_OFFSET_Y` на 30. Как изменилось положение текста?"  

*(Ученики экспериментируют, учитель объясняет, как подбирать значения.)*  

---

#### **6. Доработка игры (по желанию, 10–20 мин)**  
**Учитель:**  
*"Сейчас игра просто показывает карточки. Давайте улучшим её! Варианты:  
1. **Счётчик кликов**: Добавим переменную `score`, которая будет увеличиваться при клике.  
2. **Разные цвета**: Сделаем каждую карточку своего цвета.  
3. **Таймер**: Добавим отсчёт времени.  

Кто хочет попробовать? Давайте разберём первый вариант вместе!"*  

*(Пишут код для счётчика, разбирают `pygame.MOUSEBUTTONDOWN`.)*  

---

#### **7. Итоги (5 мин)**  
**Учитель:**  
*"Сегодня мы:  
1. Познакомились с PyGame.  
2. Создали игру с нуля, используя ООП.  
3. Узнали про особенности платформы.  

**Вопросы:**  
- Что было самым сложным?  
- Что понравилось больше всего?  

**Домашнее задание (на выбор):**  
1. Сделать так, чтобы карточки исчезали при клике.  
2. Добавить надпись 'Победа!' после исчезновения всех карточек.  

Молодцы! В следующий раз добавим больше игровой механики!"*  

---

### **Советы учителю:**  
1. **Если код не работает:**  
   - Проверьте отступы (особенно в классах).  
   - Убедитесь, что все константы в верхнем регистре.  

2. **Для продвинутых:**  
   - Можно добавить анимацию исчезновения карточек.  
   - Реализовать систему уровней.  

3. **Если время поджимает:**  
   - Сократите практику с FPS/цветами.  
   - Основное внимание — на классы и цикл игры.  

Эти текстовки помогут провести урок плавно и вовлечь учеников!
