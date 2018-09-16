def replace_word(word):
    string = ""
    default = {
        'J': 'e',
        'X': 't',
        'U': 'a',
        'D': 'h',
        'T': 'c',
        'O': 'f',
        'I': 'v',
        'K': 'y',
        'G': 'o',
        'C': 'u',
        'B': 'r',
        'N': 'n',
        'Q': 'l',
        'R': 'w',
        'H': 'i',
        'W': 's',
        'M': 'm',
        'E': 'q',
        'Z': 'p',
        'F': 'b',
        'V': 'g',
        'S': 'd',
        'P': 'k',
        'A': 'x',
        'L': 'z'



    }
    for i in word:
        if i in default:
            string += default[i]
        else:
            string += i
    return string

print(replace_word("XDJ MJXDGSGQGVK FJDHNS OBJECJNTK UNUQKWHW BJQHJW GN XDJ OUTX XDUX HN UNK QUNVCUVJ, JUTD QJXXJB DUW HXW GRN ZJBWGNUQHXK. XDJ MGWX GFIHGCW XBUHX XDUX QJXXJBW DUIJ HW XDJ OBJECJNTK RHXD RDHTD XDJK UZZJUB HN U QUNVCUVJ. TQJUBQK HN JNVQHWD XDJ QJXXJB 'L' UZZJUBW OUB QJWW OBJECJNXQK XDUN, WUK, 'U'. HN XHMJW VGNJ FK, HO KGC RUNXJS XG OHNS GCX XDJ OBJECJNTHJW GO QJXXJBW RHXDHN U QUNVCUVJ, KGC DUS XG OHNS U QUBVJ ZHJTJ GO XJAX UNS TGCNX JUTD OBJECJNTK. NGR, DGRJIJB, RJ DUIJ TGMZCXJBW XDUX TUN SG XDJ DUBS RGBP OGB CW. FCX HN OUTX, RJ SGN'X JIJN NJJS XG SG XDHW WXJZ, UW OGB MGWX QUNVCUVJW XDJBJ UBJ SUXUFUWJW GO XDJ QJXXJB OBJECJNTHJW, RDHTD DUIJ FJJN TUQTCQUXJS FK QGGPHNV UX MHQQHGNW GO XJAXW, UNS UBJ XDCW IJBK DHVDQK UTTCBUXJ."))