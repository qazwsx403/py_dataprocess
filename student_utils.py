# student_utils.py
def parse_student(line):
    line = line.strip()
    if not line:
        raise ValueError("空行")
    parts = line.split(",")
    if len(parts)!=2:
        raise ValueError("字段数量错误")
    name,s_str = parts
    name = name.strip()
    if len(name)==0:
        raise ValueError("姓名为空")
    score = int(s_str.strip())
    if not (0<=score<=100):
        raise ValueError(f"分数{score}不在0‑100")
    return {"name":name,"score":score}
