from core.logistics import display_schedule_and_logistics
from core.manager import register_new_flight
from utils.time_helper import calculate_flight_eta
from utils.file_helper import initialize_log_directory

# Dữ liệu chuyến bay khởi tạo ban đầu theo yêu cầu nghiệp vụ
flights = [
    {"flight_id": "RA001", "passengers": 154, "depart_time": "2026-06-15 08:00:00", "duration_min": 120},
    {"flight_id": "RA002", "passengers": 85,  "depart_time": "2026-06-15 13:30:00", "duration_min": 45}
]

def main():
    while True:
        print("\n===== HỆ THỐNG ĐIỀU HÀNH BAY RIKKEI AVIATION =====")
        print("1. Hiển thị lịch trình và Thống kê hậu cần")
        print("2. Tiếp nhận chuyến bay mới")
        print("3. Tính thời gian hạ cánh dự kiến (ETA)")
        print("4. Khởi tạo thư mục lưu trữ log hệ thống")
        print("5. Thoát chương trình")
        print("==================================================")
        
        try:
            choice_input = input("Nhập lựa chọn của bạn (1-5): ").strip()
            # Bẫy 4: Ngăn chặn ký tự lạ, chữ cái nhập vào menu gây crash
            choice = int(choice_input)
        except ValueError:
            print("🔴 LỖI: Lựa chọn không hợp lệ! Vui lòng chỉ nhập các chữ số từ 1 đến 5.")
            continue
            
        if choice == 1:
            display_schedule_and_logistics(flights)
        elif choice == 2:
            register_new_flight(flights)
        elif choice == 3:
            calculate_flight_eta(flights)
        elif choice == 4:
            initialize_log_directory("aviation_logs")
        elif choice == 5:
            print("\nCảm ơn kỹ sư đã sử dụng hệ thống! Hẹn gặp lại.")
            break
        else:
            print("🔴 LỖI: Lựa chọn nằm ngoài danh mục. Vui lòng nhập số trong khoảng từ 1-5.")

if __name__ == "__main__":
    main()