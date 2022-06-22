# 定義一個裝飾器，計算 1+2+...+max 的總和
def caculatefactory(max):
    def caculate(callback):
        def run():
            total = 0
            for n in range(max+1):
                total += n
            callback(total)
        return run
    return caculate

@caculatefactory(100)
def show(result):
    print("計算結果是", result)

@caculatefactory(10)
def showenglish(result):
    print("result is", result)

show()
showenglish()


# def myfactory(base):
#     def mydeco(cb):
#         def run():
#             print("裝飾器內的程式", base)
#             result=base * 2
#             cb(result)
#         return run
#     return mydeco

# @myfactory(5)
# def test(result):
#     print("普通函式的程式", result)

# test()