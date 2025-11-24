order_status=input('Введите состояние заказа(pending, processing, shipped, delivered, cancelled): ')

match order_status:
    case 'pending':
        status='В ожиданиии'
        description='Заказ находится в ожидании подтверждения'
        emoji='⌛'
        waiting_time='1-2 часа'
    case 'processing':
        status='В обработке'
        description='Заказ готовиться к отправке'
        emoji='📦'
        waiting_time='1-3 дня'
    case 'shipped':
        status='Отправлено'
        description='Заказ передан в службу доставки'
        emoji='🚚'
        waiting_time='3-7 дней'
    case 'delivered':
        status='Доставлено'
        description='Заказ доставлен получателю'
        emoji='✅'
        waiting_time='Заказ завершен'
    case 'cancelled':
        status='Отменено'
        description='Заказ был отменен'
        emoji='❌'
        waiting_time='Обработка отмены: 1-24 часа'
    case _:
        print('❌ Ошибка: неизвестный статус заказа')
print(f'Статус заказа: {status}')
print(f'Описание заказа: {description}')
print(emoji)
print(f'Время обработки: {waiting_time}')
