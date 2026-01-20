from selenium.webdriver.common.by import By

class MainPageLocators:
    # кнопки навигации
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']/ancestor::a")  # кнопка Конструктор
    FEED_BUTTON = (By.XPATH, "//p[text()='Лента Заказов']/ancestor::a")  # кнопка Лента Заказов

    # ингредиенты
    FLUORESCENT_BUN = (By.XPATH, ".//*[text()='Флюоресцентная булка R2-D3']")  # карточка ингредиента Флюоресцентная булка R2-D3
    INGREDIENT_COUNTER = (By.XPATH, ".//*[@class='counter_counter__num__3nue1']")  # счетчик количества выбранного ингредиента

    # модальное окно
    MODAL_WINDOW = (By.XPATH, "//h2[text()='Детали ингредиента']/parent::div")  # модальное окно с деталями ингредиента
    MODAL_CLOSE_BUTTON = (By.XPATH, "//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")  # кнопка-крестик для закрытия модального окна
    OVERLAY = (By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div")  # оверлей
    OVERLAY_ANIMATION = (By.XPATH, "//img[@alt ='loading animation']")
    MODAL_CONTENT_BOX = (By.XPATH, "//div[contains(@class, 'Modal_modal__contentBox')]")

    # корзина (для drag-and-drop)
    BASKET_LIST = (By.XPATH, "//div[contains(@class, 'constructor-element_pos_top')]")  # область верхней булки в конструкторе заказа

    # оформление заказа
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")  # кнопка Оформить заказ
    ORDER_ID = (By.XPATH, ".//h2[contains(@class, 'Modal_modal__title') and contains(@class, 'text_type_digits-large')]")  # номер заказа в модальном окне