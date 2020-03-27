with open('test.txt', 'r') as f:
    test_img_path=[]
    for line in f:
        test_img_path.append(line.strip())
print(test_img_path)
