def autograde_options(question,answer1,answer2,answer3,answeruser):
    if (answeruser.__contains__(answer1) or answeruser.__contains__(answer2) or answeruser.__contains__(answer3)):
        return True
    else:
        return False
print(autograde_options("How many roads must a man walk down?","Forty-two","forty-two","42", "Uh a lot idk"))
def autograde_multipart(question,a1,a2,a3,answer):
    if (answer.__contains__(a1) and answer.__contains__(a2) and answer.__contains__(a3)):
        return True
    else:
        return False
print(autograde_multipart("What is the equation describing a mass in motion?","mass","velocity","momentum","momentum = velocity * mass"))
