# ubuntu@num:~$ time ./blah 0b430e92-ef7c-48ba-b6a5-42e7e0c847c5.basecall.vcf > /dev/null
#
# real	0m0.221s
# user	0m0.165s
# sys	0m0.056s

import os
import memfiles

let data = memfiles.open(paramStr(1))
var buf: TaintedString = ""

proc printSlice(ms: MemSlice) =
    buf.setLen(ms.size)
    copyMem(addr(buf[0]), ms.data, ms.size)
    echo buf

proc main =
    for ms in memSlices(data):
        let cs = cast[cstring](ms.data)
        if cs[0] == '#':
            printSlice(ms)
            continue
    
        var tabs = 0
        var ch = 0
    
        while tabs != 4:
            if(cs[ch] == '\t'):
                inc tabs
            inc ch
    
        if cs[ch] != '.':
            printSlice(ms)

main()