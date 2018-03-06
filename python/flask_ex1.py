from flask import Flask
app = Flask(__name__)

@app.route("/group")
def group():
    output = ""
    with open("2a_raw.txt") as fh:
        # 逐行讀出檔案資料, 並放入數列中
        lines = fh.readlines()
        # 設法用迴圈逐數列內容取出字串
        # 組序變數 g 起始值設為 0
        g = 0
        for i in range(len(lines)):
            # 利用 strip() 去除各行字串最末端的跳行符號
            #print(lines[i].strip())
            line = lines[i].strip()
            # 利用 split() 將以 \t 區隔的字串資料分離後納入 groups 字串
            groups = line.split("\t")
            #print(groups)
            for i in range(len(groups)):
                # 每組有三名組員
                if i%3 == 0:
                    # 每三位組員組序增量 1
                    g += 1
                    #print()
                    output += "<br />"
                    #print("第" + str(g) + "組:")
                    output += "第" + str(g) + "組:"
                    #print(groups[i])
                    output += groups[i] + " "
                else:
                   output += groups[i] + " "
    return output
    
@app.route("/seat")
def hello():
    return "Hello World!"
    
app.run(host="192.168.1.31")
