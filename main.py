def pars_txt_to_XML(this_filename):
    AS_FileVersion = "4.9"  # Версия AutomationStudio_FileVersion в используемой студии старшей версии
    f = open(f'./Data_txt/{this_filename}', 'r')
    new_xml = ""
    NumTub = 0
    Tab = '  '
    for line in f:
        line = line.lstrip()
        if line.find('<?xml') != -1:
            new_xml += f'{Tab * NumTub}<?xml version="1.0" encoding="utf-8"?>\n<?AutomationStudio FileVersion="{AS_FileVersion}"?>\n<AcoposParameterTable>\n'
            NumTub += 1
            new_xml += f'{Tab * NumTub}<Root Name="Parameters">\n'
            NumTub += 1
        if line.find('<Group') != -1:
            Name = line[line.find('"'): line.rfind('"') + 1: 1]
            Name = Name.replace('Remark', 'Description')
            new_xml += f'{Tab * NumTub}<Group Name={Name}>\n'
            NumTub += 1
        if line.find('</Group>') != -1:
            NumTub -= 1
            new_xml += NumTub * Tab + line
        if line.find('<Parameter') != -1:
            new_xml += NumTub * Tab + line.replace('Remark', 'Description')

        if line.find('</AcoposParameters>') != -1:
            NumTub -= 1
            new_xml += NumTub * Tab + '</Root>\n'
            NumTub -= 1
            new_xml += NumTub * Tab + '</AcoposParameterTable>'
    f.close
    this_filename = this_filename.replace('txt', 'xml')
    f = open(f'./Result_xml/{this_filename}', 'w')
    f.write(new_xml)
    f.close


if __name__ == '__main__':
    import os
    for root, dirs, files in os.walk("./Data_txt"):
        for filename in files:
            if filename.endswith(".txt"):
                print(filename)
                pars_txt_to_XML(filename)
