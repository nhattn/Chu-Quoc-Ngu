# Chữ quốc ngữ

> Hiện tại khi xây dựng hệ thống máy học nếu xây dựng bộ từ điển với các
từ đơn sẽ làm quá trình truy xuất tập tin nhiều và có khi không thể liệt
kê được hết tất cả các từ đơn của tiếng việt vì vậy đoạn mã nhỏ gọn này có
thể giúp chúng ta sẽ nhận diện được chữ quốc ngữ mà không cần phải truy 
xuất từ trong từ điển.

Tài liệu tham khảo từ tập tin `chu-quoc-ngu.md` được trích xuất ngắn gọn
phần kiểm tra tính đúng đắn của một từ nhập vào, hiện tại chưa kiểm tra
chính xác được hoàn toàn nếu như có các đưa dữ liệu vào kiểu `telex` như
`tooi nosi (nois) đoofng baof cos nghe rox howm` hoặc kiểu `vni` như sau
`to6i no1i d9o6ng2 ...` cho nên để tính đúng đắn thì cần xử lý việc này
trước khi kiểm tra.

Cú pháp sử dụng `isVNESE(word)` hàm này sẽ trả về `True` hoặc `False` ví dụ

```python
isVNESE('đồ') # True
isVNESE('mi') # True
isVNESE('là') # True
isVNESE('đồ') # True
isVNESE('mi') # True
isVNESE('phá') # True
isVNESE('ba') # True
isVNESE('mi') # True
isVNESE('về') # True
isVNESE('là') # True
isVNESE('ba') # True
isVNESE('mi') # True
isVNESE('la') # True
isVNESE('olala') # False
isVNESE('.') # True
```

Ngoài ra chúng ta cũng có **nhập nhằng** khi lẫn lộn từ chung với tiếng anh
ví dụ như từ `to` (đến) `to` (to lớn) "welcome `to` vietnam" `<>` "cao `to`
đẹp choai"

Để xử lý việc này chúng ta sẽ sử dụng từ lân cận của nó để xác định.
