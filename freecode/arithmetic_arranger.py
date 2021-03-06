def arithmetic_arranger(problems, answer=False):

    problem = [i.split(" ") for i in problems]

    #errors
    if len(problems) > 5:
        return "Error: Too many problems."
    for i in problem:
        if i[1] in "%*/":
            return "Error: Operator must be '+' or '-'."
    for i in ' '.join(problems):
        if i not in "1234567890 +-":
            return "Error: Numbers must only contain digits."
    for i in problem:
        if len(i[0]) > 4:
            return "Error: Numbers cannot be more than four digits"
        if len(i[2]) > 4:
            return "Error: Numbers cannot be more than four digits"

    num1 = []
    operator = []
    num2 = []
    ans = []

    for i in problem:
        num1.append(i[0])
        operator.append(i[1])
        num2.append(i[2])
        if i[1] == "+":
            ans.append(str(int(i[0]) + int(i[2])))
        if i[1] == "-":
            ans.append(str(int(i[0]) - int(i[2])))

    one = ""
    two = ""
    three = ""
    four = ""

    for i in range(len(num1) - 1):
        if len(num1[i]) >= len(num2[i]):
            one += "  " + num1[i] + 4 * " "
            two += operator[i] + " " + ((len(num1[i]) - len(num2[i])) * " ") + num2[i] + 4 * " "
            three += (2 + len(num1[i])) * "-" + 4 * " "
            four += (2 + len(num1[i]) - len(ans[i])) * " " + ans[i] + 4 * " "
        if len(num1[i]) < len(num2[i]):
            one += "  " + ((len(num2[i]) - len(num1[i])) * " ") + num1[i] + 4 * " "
            two += operator[i] + " " + num2[i] + 4 * " "
            three += (2 + len(num2[i])) * "-" + 4 * " "
            four += (2 + len(num2[i]) - len(ans[i])) * " " + ans[i] + 4 * " "

    if len(num1[-1]) >= len(num2[-1]):
        one += "  " + num1[-1]
        two += operator[-1] + " " + ((len(num1[-1]) - len(num2[-1])) * " ") + num2[-1]
        three += (2 + len(num1[-1])) * "-"
        four += (2 + len(num1[-1]) - len(ans[-1])) * " " + ans[-1]
    if len(num1[-1]) < len(num2[-1]):
        one += "  " + ((len(num2[-1]) - len(num1[-1])) * " ") + num1[-1]
        two += operator[-1] + " " + num2[-1]
        three += (2 + len(num2[-1])) * "-"
        four += (2 + len(num2[-1]) - len(ans[-1])) * " " + ans[-1]


    res =  one + "\n" + two + "\n" + three

    if answer == True:
        res += "\n" + four

    return res

print(arithmetic_arranger(["32 - 698", "3801 - 2", "45 + 43", "123 + 49"], True))

