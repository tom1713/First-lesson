# 定義一個裝飾器，計算 1+2+...+50 的總和
def caculate(callback):
    def run():
        # 裝飾器想要執行的程式碼
        result = 0
        for n in range(51):
            result += n
        # 把計算結果透過參數傳到被裝飾的普通函式中
        callback(result)
    return run

# 使用裝飾器
@caculate
def show(n):
    print("計算結果是", n)

@caculate
def showenglish(n):
    print("result is", n)

show()
showenglish()

# # 定義裝飾器
# def mydeco(cb):
#     def run():
#         print("裝飾器中的程式碼")
#         cb(3) # 這個回呼函式，其實就是被裝飾的普通函式
#     return run
# # 使用裝飾器
# @mydeco
# def test(n):
#     print ("普通函式的程式碼", n)

# test()