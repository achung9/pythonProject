from xucxac.dice import Dice
import matplotlib.pyplot as plt
def main():
    arr1 = []
    arr2 = []
    my_Dice1 = Dice(arr1)
    my_Dice2 = Dice(arr2)
    my_Dice1.roll()
    my_Dice2.roll()
    result = []
    for i in range(len(arr1)):
        result.append(arr1[i]+arr2[i])
    frequence = []
    sums = list(range(2,13))
    for i in range (2,13):
         frequence.append(countAppearance(result,i))
    for i in frequence:
        print(i)
    plt.figure(figsize=(10,6))
    bars = plt.bar(sums , frequence,color='b' , alpha = 0.7)
    plt.xlabel('Tổng giá trị 2 xúc xắc', fontsize=12)
    plt.ylabel('Xác suất xuất hiện', fontsize=12)
    plt.title(f'Phân phối xác suất sau {1000} lần đổ', fontsize=14)
    plt.xticks(sums)  # Hiển thị đầy đủ các số từ 2 đến 12 trên trục x

    # Thêm số liệu cụ thể trên đầu mỗi cột
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width() / 2, yval + 0.005, f'{yval:.3f}', ha='center', va='bottom')

    plt.grid(axis='y', linestyle='--', alpha=0.6)
    plt.show()
def countAppearance(arr,num):
    count = 0
    for i in arr:
        if i == num:
            count += 1
    return count/len(arr)
main()