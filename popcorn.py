import barcode
from barcode.writer import ImageWriter

# 바코드 생성 함수
def generate_barcode(data, filename):
    # EAN-13 형식의 바코드를 생성합니다.
    ean = barcode.get_barcode_class('ean13')

    # 바코드 객체를 생성하고 이미지로 저장합니다.
    barcode_object = ean(data, writer=ImageWriter)
    barcode_object.save(filename)

# 메뉴 1번부터 3번까지의 바코드 생성
menu_items = {
    '메뉴1번': '123456789101',  # 각 메뉴에 대한 고유한 번호 입력
    '메뉴2번': '234567891012',
    '메뉴3번': '345678910123'
}

for menu, barcode_data in menu_items.items():
    generate_barcode(barcode_data, f'{menu}_barcode')
