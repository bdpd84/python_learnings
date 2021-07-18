file_name = "write_mode.txt"

with open(file_name,"w") as file_write_obj:
    file_write_obj.write("3 Things to know when applying Machine Learning & Artificial Intelligence to QA Test Automation. Mark Moore. ..."+"\n")
    file_write_obj.write("Step 1 - Recognize Patterns in Test Automation. ...\n")
    file_write_obj.write("Step 2 - Establish Predictability in Data for Continuous Integration. ...\n")

with open(file_name,"a") as file_write_obj:
    file_write_obj.write("Step 3 – Apply Human Ingenuity to Complex Algorithms.\n")