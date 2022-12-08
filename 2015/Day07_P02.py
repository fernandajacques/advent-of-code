wireList = ['b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'aa', 'ab', 'ac', 'ad', 'ae', 'af', 'ag', 'ah', 'ai', 'aj', 'ak', 'al', 'am', 'an', 'ao', 'ap', 'aq', 'ar', 'as', 'at', 'au', 'av', 'aw', 'ax', 'ay', 'az', 'ba', 'bb', 'bc', 'bd', 'be', 'bf', 'bg', 'bh', 'bi', 'bj', 'bk', 'bl', 'bm', 'bn', 'bo', 'bp', 'bq', 'br', 'bs', 'bt', 'bu', 'bv', 'bw', 'bx', 'by', 'bz', 'ca', 'cb', 'cc', 'cd', 'ce', 'cf', 'cg', 'ch', 'ci', 'cj', 'ck', 'cl', 'cm', 'cn', 'co', 'cp', 'cq', 'cr', 'cs', 'ct', 'cu', 'cv', 'cw', 'cx', 'cy', 'cz', 'da', 'db', 'dc', 'dd', 'de', 'df', 'dg', 'dh', 'di', 'dj', 'dk', 'dl', 'dm', 'dn', 'do', 'dp', 'dq', 'dr', 'ds', 'dt', 'du', 'dv', 'dw', 'dx', 'dy', 'dz', 'ea', 'eb', 'ec', 'ed', 'ee', 'ef', 'eg', 'eh', 'ei', 'ej', 'ek', 'el', 'em', 'en', 'eo', 'ep', 'eq', 'er', 'es', 'et', 'eu', 'ev', 'ew', 'ex', 'ey', 'ez', 'fa', 'fb', 'fc', 'fd', 'fe', 'ff', 'fg', 'fh', 'fi', 'fj', 'fk', 'fl', 'fm', 'fn', 'fo', 'fp', 'fq', 'fr', 'fs', 'ft', 'fu', 'fv', 'fw', 'fx', 'fy', 'fz', 'ga', 'gb', 'gc', 'gd', 'ge', 'gf', 'gg', 'gh', 'gi', 'gj', 'gk', 'gl', 'gm', 'gn', 'go', 'gp', 'gq', 'gr', 'gs', 'gt', 'gu', 'gv', 'gw', 'gx', 'gy', 'gz', 'ha', 'hb', 'hc', 'hd', 'he', 'hf', 'hg', 'hh', 'hi', 'hj', 'hk', 'hl', 'hm', 'hn', 'ho', 'hp', 'hq', 'hr', 'hs', 'ht', 'hu', 'hv', 'hw', 'hx', 'hy', 'hz', 'ia', 'ib', 'ic', 'id', 'ie', 'if', 'ig', 'ih', 'ii', 'ij', 'ik', 'il', 'im', 'in', 'io', 'ip', 'iq', 'ir', 'is', 'it', 'iu', 'iv', 'iw', 'ix', 'iy', 'iz', 'ja', 'jb', 'jc', 'jd', 'je', 'jf', 'jg', 'jh', 'ji', 'jj', 'jk', 'jl', 'jm', 'jn', 'jo', 'jp', 'jq', 'jr', 'js', 'jt', 'ju', 'jv', 'jw', 'jx', 'jy', 'jz', 'ka', 'kb', 'kc', 'kd', 'ke', 'kf', 'kg', 'kh', 'ki', 'kj', 'kk', 'kl', 'km', 'kn', 'ko', 'kp', 'kq', 'kr', 'ks', 'kt', 'ku', 'kv', 'kw', 'kx', 'ky', 'kz', 'la', 'lb', 'lc', 'ld', 'le', 'lf', 'lg', 'lh', 'li', 'lj', 'lk', 'll', 'lm', 'ln', 'lo', 'lp', 'lq', 'lr', 'ls', 'lt', 'lu', 'lv', 'lw', 'lx', 'ly', 'lz', 'ma']
wireInputs = {}
wireValues = {'b':956}

import re

for wire in wireList:
    with open('Data_d07p01.txt', 'r') as mydata:
        for line in mydata:

            info = line.rstrip('\n')

            #compare last item to wire
            dataInfo = re.split(' ', info)
            if wire == dataInfo[-1]:
                data = re.findall('^(.*?) ->', line)

                #create a variable with the important data
                dataInput = re.split(' ', data[0])
                #print(dataInput)
                if wire == 'b':
                    continue
                else:
                    wireInputs[wire] = dataInput
            else:
                continue
#print(wireInputs)
for key in wireInputs.keys():
    
    dictValue = wireInputs.get(key)
    
    if len(dictValue) == 1:
        wireValues[key] = int(dictValue[0])

    elif 'LSHIFT' in dictValue:
        shift = int(dictValue[2])
        myValue = wireValues.get(dictValue[0])
        wireValues[key] = myValue << shift

    elif 'RSHIFT' in dictValue:
        shift = int(dictValue[2])
        myValue = wireValues.get(dictValue[0])
        wireValues[key] = myValue >> shift
    
    elif 'AND' in dictValue:

        if dictValue[0] == '1':
            myValue01 = int(dictValue[0])
            myValue02 = wireValues.get(dictValue[2])
            wireValues[key] = myValue01 & myValue02
        else:
            myValue01 = wireValues.get(dictValue[0])
            myValue02 = wireValues.get(dictValue[2])
            wireValues[key] = myValue01 & myValue02

    elif 'OR' in dictValue:
        myValue01 = wireValues.get(dictValue[0])
        myValue02 = wireValues.get(dictValue[2])
        wireValues[key] = myValue01 | myValue02
    
    elif 'NOT' in dictValue:
        myValue = wireValues.get(dictValue[1])
        wireValues[key] = 65535 - myValue

    else:
        print('I escaped it all!!! Mwahahaha')

#print(wireValues)
valueOfA = wireValues.get('lx')
print(f'lx -> a -> {valueOfA}')