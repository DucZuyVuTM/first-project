print ("Máy tính bỏ túi")
print ("Hãy hỏi người sáng lập về HDSD")
print ("Lưu ý: Tắt Telex khi dùng máy")
Ans1 = 0
def VongLapChongPhaHoai(Ans1):
    try:
        Suni = input().split(" ")
        m = 0
        while Suni.count("E") == 0:
            while Suni.count("Ans") != 0:
                Ans = Suni.index("Ans")
                Suni[Ans] = str(Ans1)
            while Suni.count("") != 0:
                Suni[Suni.index("")] = "¤"
                Suni.remove("¤")
            if (Suni[0] == "+" or Suni[0] == "-" or Suni[0] == "*" or Suni[0] == "/" or Suni[0] == "**" 
            or Suni[0] == "v" or Suni[0] == "%"):
                Suni.insert(0, str(Ans1))
            if len(Suni) == 1:
                if Suni[0] == "M+":
                    m = m + Ans1
                elif Suni[0] == "M-":
                    m = m - Ans1
                elif Suni[0] == "MR":
                    Ans1 = m
                elif Suni[0] == "MC":
                    m = 0
                else:
                    Ans1 = Suni[0]
                    if Ans1.count(".") == 1:
                        Split2 = Ans1.split(".")
                        CheckSoThapPhan = Split2[1]
                        if len(CheckSoThapPhan) > 15:
                            Ans1 = "Lỗi"
                            print ("Lỗi: Không thể nhập nhièu hơn 15 kí tự sau dấu thập phân")
                        else:
                            Ans1 = float(Ans1)
                    else:
                        Ans1 = float(Ans1)
                    if int(Ans1) == Ans1:
                        Ans1 = int(Ans1)
            while Suni.count("") != 0:
                Suni[Suni.index("")] = "¤"
                Suni.remove("¤")
            while Suni.count(")") != 0:
                e = d = Suni.index(")")
                d1 = ""
                while d1 != "(":
                    d -= 1
                    d1 = Suni[d]
                Suni2 = Suni[d+1:e]
                while Suni2.count("v") != 0:
                    can = Suni2.index("v")
                    b = Suni2[can-1]
                    if b.count(".") == 1:
                        Split2 = b.split(".")
                        CheckSoThapPhan = Split2[1]
                        if len(CheckSoThapPhan) > 15:
                            b = "Lỗi"
                            print ("Lỗi: Không thể nhập nhièu hơn 15 kí tự sau dấu thập phân")
                        else:
                            b = float(b)
                    else:
                        b = float(b)
                    c = Suni2[can+1]
                    if c.count(".") == 1:
                        Split2 = c.split(".")
                        CheckSoThapPhan = Split2[1]
                        if len(CheckSoThapPhan) > 15:
                            c = "Lỗi"
                            print ("Lỗi: Không thể nhập nhièu hơn 15 kí tự sau dấu thập phân")
                        else:
                            c = float(c)
                    else:
                        c = float(c)
                    Ans1 = round(c ** (1/b), 15)
                    Ans1_check = str(Ans1)
                    if Ans1_check.count("e") == 0:
                        Ans1 = round(Ans1, 12)
                    if int(Ans1) == Ans1:
                        Ans1 = int(Ans1)
                    Suni2.insert(can-1, str(Ans1))
                    can1 = can + 2
                    while can <= can1:
                        Suni2[can1] = "¤"
                        Suni2.remove("¤")
                        can1 -= 1
                while Suni2.count("**") != 0:
                    luythua = Suni2.index("**")
                    b = Suni2[luythua-1]
                    if b.count(".") == 1:
                        Split2 = b.split(".")
                        CheckSoThapPhan = Split2[1]
                        if len(CheckSoThapPhan) > 15:
                            b = "Lỗi"
                            print ("Lỗi: Không thể nhập nhièu hơn 15 kí tự sau dấu thập phân")
                        else:
                            b = float(b)
                    else:
                        b = float(b)
                    c = Suni2[luythua+1]
                    if c.count(".") == 1:
                        Split2 = c.split(".")
                        CheckSoThapPhan = Split2[1]
                        if len(CheckSoThapPhan) > 15:
                            c = "Lỗi"
                            print ("Lỗi: Không thể nhập nhièu hơn 15 kí tự sau dấu thập phân")
                        else:
                            c = float(c)
                    else:
                        c = float(c)
                    Ans1 = round(b ** c, 15)
                    Ans1_check = str(Ans1)
                    if Ans1_check.count("e") == 0:
                        Ans1 = round(Ans1, 12)
                    if int(Ans1) == Ans1:
                        Ans1 = int(Ans1)
                    Suni2.insert(luythua-1, str(Ans1))
                    luythua1 = luythua + 2
                    while luythua <= luythua1:
                        Suni2[luythua1] = "¤"
                        Suni2.remove("¤")
                        luythua1 -= 1
                while Suni2.count("%") != 0:
                    phantram = Suni2.index("%")
                    b = Suni2[phantram-1]
                    if b.count(".") == 1:
                        Split2 = b.split(".")
                        CheckSoThapPhan = Split2[1]
                        if len(CheckSoThapPhan) > 15:
                            b = "Lỗi"
                            print ("Lỗi: Không thể nhập nhièu hơn 15 kí tự sau dấu thập phân")
                        else:
                            b = float(b)
                    else:
                        b = float(b)
                    Ans1 = round(b / 100, 15)
                    if int(Ans1) == Ans1:
                        Ans1 = int(Ans1)
                    Suni2[phantram-1] = str(Ans1)
                    Suni2[phantram] = "¤"
                    Suni2.remove("¤")
                    phantram -= 1
                while Suni2.count("*") != 0 and Suni2.count("/") != 0:
                    nhan = Suni2.index("*")
                    chia = Suni2.index("/")
                    if nhan < chia:
                        b = Suni2[nhan-1]
                        if b.count(".") == 1:
                            Split2 = b.split(".")
                            CheckSoThapPhan = Split2[1]
                            if len(CheckSoThapPhan) > 15:
                                b = "Lỗi"
                                print ("Lỗi: Không thể nhập nhièu hơn 15 kí tự sau dấu thập phân")
                            else:
                                b = float(b)
                        else:
                            b = float(b)
                        c = Suni2[nhan+1]
                        if c.count(".") == 1:
                            Split2 = c.split(".")
                            CheckSoThapPhan = Split2[1]
                            if len(CheckSoThapPhan) > 15:
                                c = "Lỗi"
                                print ("Lỗi: Không thể nhập nhièu hơn 15 kí tự sau dấu thập phân")
                            else:
                                c = float(c)
                        else:
                            c = float(c)
                        Ans1 = round(b * c, 15)
                        Ans1_check = str(Ans1)
                        if Ans1_check.count("e") == 0:
                            Ans1 = round(Ans1, 12)
                        if int(Ans1) == Ans1:
                            Ans1 = int(Ans1)
                        Suni2.insert(nhan-1, str(Ans1))
                        nhan1 = nhan + 2
                        while nhan <= nhan1:
                            Suni2[nhan1] = "¤"
                            Suni2.remove("¤")
                            nhan1 -= 1
                    elif chia < nhan:
                        b = Suni2[chia-1]
                        if b.count(".") == 1:
                            Split2 = b.split(".")
                            CheckSoThapPhan = Split2[1]
                            if len(CheckSoThapPhan) > 15:
                                b = "Lỗi"
                                print ("Lỗi: Không thể nhập nhièu hơn 15 kí tự sau dấu thập phân")
                            else:
                                b = float(b)
                        else:
                            b = float(b)
                        c = Suni2[chia+1]
                        if c.count(".") == 1:
                            Split2 = c.split(".")
                            CheckSoThapPhan = Split2[1]
                            if len(CheckSoThapPhan) > 15:
                                c = "Lỗi"
                                print ("Lỗi: Không thể nhập nhièu hơn 15 kí tự sau dấu thập phân")
                            else:
                                c = float(c)
                        else:
                            c = float(c)
                        if c == 0:
                            print ("Lỗi: Không thể chia cho 0")
                        Ans1 = round(b / c, 15)
                        if int(Ans1) == Ans1:
                            Ans1 = int(Ans1)
                        Suni2.insert(chia-1, str(Ans1))
                        chia1 = chia + 2
                        while chia <= chia1:
                            Suni2[chia1] = "¤"
                            Suni2.remove("¤")
                            chia1 -= 1
                while Suni2.count("*") != 0:
                    nhan = Suni2.index("*")
                    b = Suni2[nhan-1]
                    if b.count(".") == 1:
                        Split2 = b.split(".")
                        CheckSoThapPhan = Split2[1]
                        if len(CheckSoThapPhan) > 15:
                            b = "Lỗi"
                            print ("Lỗi: Không thể nhập nhièu hơn 15 kí tự sau dấu thập phân")
                        else:
                            b = float(b)
                    else:
                        b = float(b)
                    c = Suni2[nhan+1]
                    if c.count(".") == 1:
                        Split2 = c.split(".")
                        CheckSoThapPhan = Split2[1]
                        if len(CheckSoThapPhan) > 15:
                            c = "Lỗi"
                            print ("Lỗi: Không thể nhập nhièu hơn 15 kí tự sau dấu thập phân")
                        else:
                            c = float(c)
                    else:
                        c = float(c)
                    Ans1 = round(b * c, 15)
                    Ans1_check = str(Ans1)
                    if Ans1_check.count("e") == 0:
                        Ans1 = round(Ans1, 12)
                    if int(Ans1) == Ans1:
                        Ans1 = int(Ans1)
                    Suni2.insert(nhan-1, str(Ans1))
                    nhan1 = nhan + 2
                    while nhan <= nhan1:
                        Suni2[nhan1] = "¤"
                        Suni2.remove("¤")
                        nhan1 -= 1
                while Suni2.count("/") != 0:
                    chia = Suni2.index("/")
                    b = Suni2[chia-1]
                    if b.count(".") == 1:
                        Split2 = b.split(".")
                        CheckSoThapPhan = Split2[1]
                        if len(CheckSoThapPhan) > 15:
                            b = "Lỗi"
                            print ("Lỗi: Không thể nhập nhièu hơn 15 kí tự sau dấu thập phân")
                        else:
                            b = float(b)
                    else:
                        b = float(b)
                    c = Suni2[chia+1]
                    if c.count(".") == 1:
                        Split2 = c.split(".")
                        CheckSoThapPhan = Split2[1]
                        if len(CheckSoThapPhan) > 15:
                            c = "Lỗi"
                            print ("Lỗi: Không thể nhập nhièu hơn 15 kí tự sau dấu thập phân")
                        else:
                            c = float(c)
                    else:
                        c = float(c)
                    if c == 0:
                        print ("Lỗi: Không thể chia cho 0")
                    Ans1 = round(b / c, 15)
                    if int(Ans1) == Ans1:
                        Ans1 = int(Ans1)
                    Suni2.insert(chia-1, str(Ans1))
                    chia1 = chia + 2
                    while chia <= chia1:
                        Suni2[chia1] = "¤"
                        Suni2.remove("¤")
                        chia1 -= 1
                ll = len(Suni2) - 1
                while ll != 0:
                    b = Suni2[0]
                    if b.count(".") == 1:
                        Split2 = b.split(".")
                        CheckSoThapPhan = Split2[1]
                        if len(CheckSoThapPhan) > 15:
                            b = "Lỗi"
                            print ("Lỗi: Không thể nhập nhièu hơn 15 kí tự sau dấu thập phân")
                        else:
                            b = float(b)
                    else:
                        b = float(b)
                    c = Suni2[2]
                    if c.count(".") == 1:
                        Split2 = c.split(".")
                        CheckSoThapPhan = Split2[1]
                        if len(CheckSoThapPhan) > 15:
                            c = "Lỗi"
                            print ("Lỗi: Không thể nhập nhièu hơn 15 kí tự sau dấu thập phân")
                        else:
                            c = float(c)
                    else:
                        c = float(c)
                    if Suni2[1] == "+":
                        Ans1 = round(b + c, 15)
                        Ans1_check = str(Ans1)
                        if Ans1_check.count("e") == 0:
                            Ans1 = round(Ans1, 14)
                        if int(Ans1) == Ans1:
                            Ans1 = int(Ans1)
                    elif Suni2[1] == "-":
                        Ans1 = round(b - c, 15)
                        Ans1_check = str(Ans1)
                        if Ans1_check.count("e") == 0:
                            Ans1 = round(Ans1, 14)
                        if int(Ans1) == Ans1:
                            Ans1 = int(Ans1)
                    else:
                        b = "Lỗi"
                        Ans1 = b - c
                    Suni2.insert(0, str(Ans1))
                    ll1 = 3
                    while ll1 != 0:
                        Suni2[ll1] = "¤"
                        Suni2.remove("¤")
                        ll1 -= 1
                    ll = len(Suni2) - 1
                Suni.insert(d, str(Ans1))
                e += 1
                while d != e:
                    Suni[e] = "¤"
                    Suni.remove("¤")
                    e -= 1
            while Suni.count("v") != 0:
                can = Suni.index("v")
                b = Suni[can-1]
                if b.count(".") == 1:
                    Split2 = b.split(".")
                    CheckSoThapPhan = Split2[1]
                    if len(CheckSoThapPhan) > 15:
                        b = "Lỗi"
                        print ("Lỗi: Không thể nhập nhièu hơn 15 kí tự sau dấu thập phân")
                    else:
                        b = float(b)
                else:
                    b = float(b)
                c = Suni[can+1]
                if c.count(".") == 1:
                    Split2 = c.split(".")
                    CheckSoThapPhan = Split2[1]
                    if len(CheckSoThapPhan) > 15:
                        c = "Lỗi"
                        print ("Lỗi: Không thể nhập nhièu hơn 15 kí tự sau dấu thập phân")
                    else:
                        c = float(c)
                else:
                    c = float(c)
                Ans1 = round(c ** (1/b), 15)
                Ans1_check = str(Ans1)
                if Ans1_check.count("e") == 0:
                    Ans1 = round(Ans1, 12)
                if int(Ans1) == Ans1:
                    Ans1 = int(Ans1)
                Suni.insert(can-1, str(Ans1))
                can1 = can + 2
                while can <= can1:
                    Suni[can1] = "¤"
                    Suni.remove("¤")
                    can1 -= 1
            while Suni.count("**") != 0:
                luythua = Suni.index("**")
                b = Suni[luythua-1]
                if b.count(".") == 1:
                    Split2 = b.split(".")
                    CheckSoThapPhan = Split2[1]
                    if len(CheckSoThapPhan) > 15:
                        b = "Lỗi"
                        print ("Lỗi: Không thể nhập nhièu hơn 15 kí tự sau dấu thập phân")
                    else:
                        b = float(b)
                else:
                    b = float(b)
                c = Suni[luythua+1]
                if c.count(".") == 1:
                    Split2 = c.split(".")
                    CheckSoThapPhan = Split2[1]
                    if len(CheckSoThapPhan) > 15:
                        c = "Lỗi"
                        print ("Lỗi: Không thể nhập nhièu hơn 15 kí tự sau dấu thập phân")
                    else:
                        c = float(c)
                else:
                    c = float(c)
                Ans1 = round(b ** c, 15)
                Ans1_check = str(Ans1)
                if Ans1_check.count("e") == 0:
                    Ans1 = round(Ans1, 12)
                if int(Ans1) == Ans1:
                    Ans1 = int(Ans1)
                Suni[luythua] = str(Ans1)
                Suni[luythua+1] = "¤"
                Suni.remove("¤")
                Suni[luythua-1] = "¤"
                Suni.remove("¤")
                luythua -= 1
            while Suni.count("%") != 0:
                phantram = Suni.index("%")
                b = Suni[phantram-1]
                if b.count(".") == 1:
                    Split2 = b.split(".")
                    CheckSoThapPhan = Split2[1]
                    if len(CheckSoThapPhan) > 15:
                        b = "Lỗi"
                        print ("Lỗi: Không thể nhập nhièu hơn 15 kí tự sau dấu thập phân")
                    else:
                        b = float(b)
                else:
                    b = float(b)
                Ans1 = round(b / 100, 15)
                if int(Ans1) == Ans1:
                    Ans1 = int(Ans1)
                Suni[phantram-1] = str(Ans1)
                Suni[phantram] = "¤"
                Suni.remove("¤")
                phantram -= 1
            while Suni.count("*") != 0 and Suni.count("/") != 0:
                nhan = Suni.index("*")
                chia = Suni.index("/")
                if nhan < chia:
                    b = Suni[nhan-1]
                    if b.count(".") == 1:
                        Split2 = b.split(".")
                        CheckSoThapPhan = Split2[1]
                        if len(CheckSoThapPhan) > 15:
                            b = "Lỗi"
                            print ("Lỗi: Không thể nhập nhièu hơn 15 kí tự sau dấu thập phân")
                        else:
                            b = float(b)
                    else:
                        b = float(b)
                    c = Suni[nhan+1]
                    if b.count(".") == 1:
                        Split2 = b.split(".")
                        CheckSoThapPhan = Split2[1]
                        if len(CheckSoThapPhan) > 15:
                            b = "Lỗi"
                            print ("Lỗi: Không thể nhập nhièu hơn 15 kí tự sau dấu thập phân")
                        else:
                            b = float(b)
                    else:
                        b = float(b)
                    Ans1 = round(b * c, 15)
                    Ans1_check = str(Ans1)
                    if Ans1_check.count("e") == 0:
                        Ans1 = round(Ans1, 12)
                    if int(Ans1) == Ans1:
                        Ans1 = int(Ans1)
                    Suni[nhan] = str(Ans1)
                    Suni[nhan+1] = "¤"
                    Suni.remove("¤")
                    Suni[nhan-1] = "¤"
                    Suni.remove("¤")
                    nhan -= 1
                elif chia < nhan:
                    b = Suni[chia-1]
                    if b.count(".") == 1:
                        Split2 = b.split(".")
                        CheckSoThapPhan = Split2[1]
                        if len(CheckSoThapPhan) > 15:
                            b = "Lỗi"
                            print ("Lỗi: Không thể nhập nhièu hơn 15 kí tự sau dấu thập phân")
                        else:
                            b = float(b)
                    else:
                        b = float(b)
                    c = Suni[chia+1]
                    if c.count(".") == 1:
                        Split2 = c.split(".")
                        CheckSoThapPhan = Split2[1]
                        if len(CheckSoThapPhan) > 15:
                            c = "Lỗi"
                            print ("Lỗi: Không thể nhập nhièu hơn 15 kí tự sau dấu thập phân")
                        else:
                            c = float(c)
                    else:
                        c = float(c)
                    if c == 0:
                        print ("Lỗi: Không thể chia cho 0")
                    Ans1 = round(b / c, 15)
                    if int(Ans1) == Ans1:
                        Ans1 = int(Ans1)
                    Suni[chia] = str(Ans1)
                    Suni[chia+1] = "¤"
                    Suni.remove("¤")
                    Suni[chia-1] = "¤"
                    Suni.remove("¤")
                    chia -= 1
            while Suni.count("*") != 0:
                nhan = Suni.index("*")
                b = Suni[nhan-1]
                if b.count(".") == 1:
                    Split2 = b.split(".")
                    CheckSoThapPhan = Split2[1]
                    if len(CheckSoThapPhan) > 15:
                        b = "Lỗi"
                        print ("Lỗi: Không thể nhập nhièu hơn 15 kí tự sau dấu thập phân")
                    else:
                        b = float(b)
                else:
                    b = float(b)
                c = Suni[nhan+1]
                if c.count(".") == 1:
                    Split2 = c.split(".")
                    CheckSoThapPhan = Split2[1]
                    if len(CheckSoThapPhan) > 15:
                        c = "Lỗi"
                        print ("Lỗi: Không thể nhập nhièu hơn 15 kí tự sau dấu thập phân")
                    else:
                        c = float(c)
                else:
                    c = float(c)
                Ans1 = round(b * c, 15)
                Ans1_check = str(Ans1)
                if Ans1_check.count("e") == 0:
                    Ans1 = round(Ans1, 12)
                if int(Ans1) == Ans1:
                    Ans1 = int(Ans1)
                Suni[nhan] = str(Ans1)
                Suni[nhan+1] = "¤"
                Suni.remove("¤")
                Suni[nhan-1] = "¤"
                Suni.remove("¤")
                nhan -= 1
            while Suni.count("/") != 0:
                chia = Suni.index("/")
                b = Suni[chia-1]
                if b.count(".") == 1:
                    Split2 = b.split(".")
                    CheckSoThapPhan = Split2[1]
                    if len(CheckSoThapPhan) > 15:
                        b = "Lỗi"
                        print ("Lỗi: Không thể nhập nhièu hơn 15 kí tự sau dấu thập phân")
                    else:
                        b = float(b)
                else:
                    b = float(b)
                c = Suni[chia+1]
                if c.count(".") == 1:
                    Split2 = c.split(".")
                    CheckSoThapPhan = Split2[1]
                    if len(CheckSoThapPhan) > 15:
                        c = "Lỗi"
                        print ("Lỗi: Không thể nhập nhièu hơn 15 kí tự sau dấu thập phân")
                    else:
                        c = float(c)
                else:
                    c = float(c)
                if c == 0:
                    print ("Lỗi: Không thể chia cho 0")
                Ans1 = round(b / c, 15)
                if int(Ans1) == Ans1:
                    Ans1 = int(Ans1)
                Suni[chia] = str(Ans1)
                Suni[chia+1] = "¤"
                Suni.remove("¤")
                Suni[chia-1] = "¤"
                Suni.remove("¤")
                chia -= 1
            l = len(Suni) - 1
            while l != 0:
                b = Suni[0]
                if b.count(".") == 1:
                    Split2 = b.split(".")
                    CheckSoThapPhan = Split2[1]
                    if len(CheckSoThapPhan) > 15:
                        b = "Lỗi"
                        print ("Lỗi: Không thể nhập nhièu hơn 15 kí tự sau dấu thập phân")
                    else:
                        b = float(b)
                else:
                    b = float(b)
                c = Suni[2]
                if c.count(".") == 1:
                    Split2 = c.split(".")
                    CheckSoThapPhan = Split2[1]
                    if len(CheckSoThapPhan) > 15:
                        c = "Lỗi"
                        print ("Lỗi: Không thể nhập nhièu hơn 15 kí tự sau dấu thập phân")
                    else:
                        c = float(c)
                else:
                    c = float(c)
                if Suni[1] == "+":
                    Ans1 = round(b + c, 15)
                    Ans1_check = str(Ans1)
                    if Ans1_check.count("e") == 0:
                        Ans1 = round(Ans1, 14)
                    if int(Ans1) == Ans1:
                        Ans1 = int(Ans1)
                elif Suni[1] == "-":
                    Ans1 = round(b - c, 14)
                    Ans1_check = str(Ans1)
                    if Ans1_check.count("e") == 0:
                        Ans1 = round(Ans1, 14)
                    if int(Ans1) == Ans1:
                        Ans1 = int(Ans1)
                else:
                    b = "Lỗi"
                    Ans1 = b - c
                Suni[1] = str(Ans1)
                Suni[2] = "¤"
                Suni.remove("¤")
                Suni[0] = "¤"
                Suni.remove("¤")
                l = len(Suni) - 1
            Ans1_str = str(Ans1)
            if Ans1_str.count("e") == 0:
                Ans1_thapphan = "."
                if Ans1_str.count(".") == 1:
                    Ans1_split = Ans1_str.split(".")
                    Ans1_hienthi = Ans1_split[0]
                    Ans1_thapphan += Ans1_split[1]
                else:
                    Ans1_hienthi = Ans1_str
                Suni_spec = []
                for conso in Ans1_hienthi:
                    Suni_spec.append(conso)
                Sln = -(len(Suni_spec))
                dauphay = -3
                while Sln < dauphay:
                    Suni_spec.insert(dauphay, ",")
                    dauphay -= 4
                    Sln = -(len(Suni_spec))
                Suni_spec = ''.join(Suni_spec)
                if Ans1_thapphan != ".":
                    Suni_spec += Ans1_thapphan
            else:
                Suni_spec = Ans1_str
            print ("=", Suni_spec)
            Suni = input().split(" ")
        print ("Đã tắt máy tính")
    except:
        print ("Có lỗi xảy ra, vui lòng nhập lại!")
        Ans1 = 0
        VongLapChongPhaHoai(Ans1)
VongLapChongPhaHoai(Ans1)
