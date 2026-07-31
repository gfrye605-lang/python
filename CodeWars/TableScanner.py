x = ['good', 'good', 'good']

scanning = True

def well(x):
    while scanning:
        b_count = x.count("bad") 
        g_count = x.count("good")
        if b_count > 0 and g_count > 0:
            verdict = "Pass"
        elif b_count == 0 and g_count > 0:
            verdict = "I smell a series!"
        elif b_count > 0 and g_count == 0:
            verdict = "Fail"
        else:
            verdict = "Neither good nor bad."
        print("Verdict: ", verdict)
        return verdict

well(x)