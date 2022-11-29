 #                                                                :revolving_hearts:WEB CLIENT SOCKET:revolving_hearts:
 ##                                             💘 Đồ án thực hạnh mạng máy tính - Đề 02 : Web Client

**_:face_in_clouds:   GIỚI THIỆU :_**
Mục tiêu là viết một web client đơn giản. Web client sẽ gửi request đến web server, port 80 để tại nội dung của page và lưu vào file .

**_:face_in_clouds:   HANDLE CONNECTION CƠ BẢN ._**


  **:pouting_cat: Client tạo một TCP socket, kết nối đến port 80 của web server. Sau khi kết nối đến web server, client sẽ gửi request đến web server để tải page.**
 
  **:pouting_cat: Client yêu cầu sử dụng HTTP/1.1 và "Connection: keep-alive", khi đó hàm "recv" sẽ vẫn chờ nhận dữ liệu mặc dù đã nhận đủ nội dung file.** 
 
  **:pouting_cat: Ta cần tính toán để biết khi nào đã nhận xong data và đóng kết nối. Vậy làm sao Client có thể biết được là đã nhận đủ data, thì bạn dựa vào một trong      các trường hợp:**

   + **"Content-Length:" cho biết nội dung của body**
        
   + **"Transfer-Encoding: chunked", khi đó webserver sẽ trả về dữ liệu từng chunk, làm sao nhận biết được độ dài 1 chunk và khi nào nhận hết các chunk,**
       Tham khảo: https://en.wikipedia.org/wiki/Chunked_transfer_encoding, https://bunny.net/academy/http/what-is-chunked-encoding/


**_:face_in_clouds:   MÔI TRƯỜNG LẬP TRÌNH VÀ ỨNG DỤNG ._**
    
   **• Ứng dụng được viết trên hệ điều hành Windows 11 .**
   
   **• Ngôn ngữ lập trình : Python 3 . • IDE sử dụng : Visual Studio Code.**
   
   **• Các dữ liệu được lưu trữ tại các folder theo yêu cầu .**
   
   **• Thư viện hỗ trợ : socket , sys, threading ,os.path , bs4 from BeautifulSoup , string.**
   
 
_**:face_in_clouds:    HƯỚNG DẪN SỬ DỤNG .**_
   
  _**:ghost:  1 . Tải và lưu file hay các folder với các chức năng cơ bản   =>   Sử dụng file run_basic.py**_ 
  
  ![1](https://user-images.githubusercontent.com/100368114/204431490-8bd04b63-bb69-4952-acce-59a323ba854e.jpg)

  _**:ghost:  2 . Tải vầ lưu file ở các chức năng nâng cao  => Sử dụng các file multiple_connection.py hoặc multiple_requests.py**_
  
   ![2](https://user-images.githubusercontent.com/100368114/204431246-7a9ab6db-0613-4e52-ab79-352329dead4f.jpg)
    
  _**:ghost:  3 . Chú ý : Các máy tính phải được cài đặt môi trường cho python .**_
 
    
