import os.path

with open("vrep_35rev3_dll.txt") as fh:
    # 逐行讀出檔案資料, 並放入數列中
    lines = fh.readlines()
    # 設法用迴圈逐數列內容取出字串
    # 組序變數 g 起始值設為 0
    g = 0
    for i in range(len(lines)):
        # 利用 strip() 去除各行字串最末端的跳行符號
        #print(lines[i].strip())
        line = lines[i].strip()
        # 利用 split() 將以 space 區隔的字串資料分離後納入 groups 字串
        groups = line.split()[2]
        if not os.path.isfile(groups):
            print(groups)