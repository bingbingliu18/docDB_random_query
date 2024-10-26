import sys

def calculate_average(file_path):
    try:
        # 打开文件
        with open(file_path, 'r') as file:
            # 初始化总和和行数
            total = 0
            count = 0

            # 遍历每一行
            for line in file:
                # 尝试将行转换为浮点数
                try:
                    value = float(line.strip())
                    total += value
                    count += 1
                # 如果转换失败,忽略该行
                except ValueError:
                    pass

            # 计算平均值
            if count > 0:
                average = total / count
                print(f"平均值为: {average}")
                print(f"Total Count: {count}")
            else:
                print("文件为空或者没有有效数值")

    except FileNotFoundError:
        print(f"文件 {file_path} 不存在")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("使用方法: python script.py <file_path>")
    else:
        file_path = sys.argv[1]
        calculate_average(file_path)

