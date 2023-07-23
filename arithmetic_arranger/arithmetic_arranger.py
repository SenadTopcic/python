def arithmetic_arranger(problems, option=False):
    if not type(problems) == list :
        arranged_problems = list()
        arranged_problems.append(problems)
    else :
        arranged_problems = problems
#checking for errors 
    if error_checking(arranged_problems) == 1:
        return "Error: Too many problems."
    elif error_checking(arranged_problems) == 2:
        return "Error: Operator must be '+' or '-'."
    elif error_checking(arranged_problems) == 3:
        return "Error: Numbers must only contain digits."
    elif error_checking(arranged_problems) == 4:   
        return "Error: Numbers cannot be more than four digits."

    # Declaration of variables
    numerator = list()
    denominator = list()
    m_denominator = list()
    operator = list()
    result = list()

    line_numerator = "" 
    line_denominator = ""
    line_dashes = ""
    line_result = ""

    for problem in arranged_problems :
        tmp_var = problem.split()
        numerator.append(tmp_var[0])
        denominator.append(tmp_var[2])
        operator.append(tmp_var[1])
        res = 0
        if tmp_var[1] == '+' :
            res = int(tmp_var[0]) + int(tmp_var[2])
        else :
            res = int(tmp_var[0]) - int(tmp_var[2])
        result.append(res) 
    m_denominator = modify_denominator(arranged_problems,denominator,numerator, operator)    
    i = 0
    distance = 0
    
    for i in range(0, len(numerator)) :
        if i == 0:
            distance = len(m_denominator[i])
            line_numerator = f"{numerator[i]:>{distance}}"
            line_denominator = f"{m_denominator[i]:>{distance}}"
            dashes = '-'* distance
            line_dashes = f"{dashes:>{distance}}"
            line_result = f"{result[i]:>{distance}}"
        elif i < len(numerator) :
            distance = len(m_denominator[i]) + 4
            line_numerator = line_numerator + f"{numerator[i]:>{distance}}"
            line_denominator = line_denominator + f"{m_denominator[i]:>{distance}}"
            dashes = '-'* (distance - 4)
            line_dashes = line_dashes + f"{dashes:>{distance}}"
            line_result = line_result + f"{result[i]:>{distance}}"


    if option :
        return (line_numerator + '\n' + line_denominator + '\n' + line_dashes  + '\n' + line_result)
    else :
        return (line_numerator + '\n' + line_denominator + '\n' + line_dashes)

 

# Check for errors ()
def error_checking(arranged_problems):
    # Error checking - maximum alowed problems
    if len(arranged_problems) > 5 :
        return 1
    for problem in arranged_problems:
        tmp_str = problem.split()
    # Error checking for operator
        if  tmp_str[1] != "+" and tmp_str[1] != "-":
            return 2
    # Error checking for operand  - are they numbers
        if not tmp_str[0].isdigit() or not tmp_str[2].isdigit():
            return 3
    # Error checking for number of alowed digits
        if len(tmp_str[0]) > 4 or len(tmp_str[2]) > 4 :
            return 4
    
# This function modify denominator adding a sign in front of number
def modify_denominator( arranged_problems, denominator, numerator, operator):
    i = 0
    mod_den = list()
    for i in range(0, len(arranged_problems)):
        if len(denominator[i]) > len(numerator[i]) :
            max_num_len = len(denominator[i]) + 2
        else :
            max_num_len = len(numerator[i]) + 2

        tmp_str = "{}{}{}"
        nbm_spcs = max_num_len - 1 - len(denominator[i])
        empty_spaces = " " * nbm_spcs
        tmp_str = tmp_str.format( operator[i], empty_spaces, denominator[i])
        mod_den.append(tmp_str)
    return  mod_den
