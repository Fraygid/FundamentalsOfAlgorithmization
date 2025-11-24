order_status=input('Введите состояние заказа(pending, processing, shipped, delivered, cancelled')

match order_status:
    case 'pending':
        status='В ожиданиии'
        description='Заказ находится в ожидании подтверждения'
        emoji='⌛'
        waiting_time='1-2 часа'
    case 'processing':
        status='В обработке'
        description='Закза готовиться к отправке'
        emoji='📦'
        waiting_time='1-3 дня'
    case 'shipped':
        status='Отправлено'
        description='Заказ передан в службу доставки'
        emoji='🚚'
        waiting_time='3-7 дней'
