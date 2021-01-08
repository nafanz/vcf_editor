import os
import vobject


class ContactList:
    def __init__(self, vcf, is_dir=False):
        self.counter = 0
        self.dic = {}
        self.active_key = ''
        self.active_value = ''
        try:
            if is_dir:  # this way counting number of files
                for file in os.listdir(vcf):
                    with open(vcf+'\\'+file, mode='r', encoding='utf-8') as vcf_file:
                        self.counter += 1
                        v = vobject.readOne(vcf_file)
                        self.append(v.n.value, str(v.tel.value).replace(' ', ''))
                        try:
                            v.fn
                        except NameError:
                            v.fn = v.n
                        # append_to_vcf(vcf + 'pokus.vcf', v)

            else:  # this way counting number of records in a file
                with open(vcf, mode='r', encoding='utf-8') as vcf_file:
                    for v in vobject.readComponents(vcf_file):
                        self.counter += 1
                        self.append(v.fn.value, str(v.tel.value).replace(' ', ''))
                        # export_to_vcf(home_folder + 'work\\', vcard)
        except Exception as e:
            print('error:', e)

    def append(self, key, value):
        print(str(self.counter)+'. '+str(key))
        self.dic[str(key)] = value

    def find_duplicates(self):
        for key, value in self.dic.items():
            self.active_key = key
            self.active_value = value
            if self.search(value):
                print('duplicate found for', key, '/', value)

    def search(self, s):
        s = s.lower()
        occurs = 0
        for name, phone in self.dic.items():
            if name != self.active_key:
                if s in name or s in phone:
                    occurs += 1
        return occurs


def export_to_vcf(location, vc):
    """
    exports vobject to a *.vcf file
    :param location: where to write
    :param vc: single vobject instance
    """
    vcf_name = vc.fn.value + '.vcf'  # .encode().decode('unicode-escape')
    with open(location + vcf_name, mode='w', encoding='utf-8') as f:
        f.write(vc.serialize())


def append_to_vcf(location, vc):
    """
    exports vobject to a *.vcf file
    :param location: where to write
    :param vc: single vobject instance
    """
    vcf_name = vc.fn.value + '.vcf'  # .encode().decode('unicode-escape')
    with open(location + vcf_name, mode='a', encoding='utf-8') as f:
        f.write(vc.serialize())

if __name__ == '__main__':
    print("O'really?")
    #home_folder = 'C:\\Users\\jirib\\Downloads\\SD_samci\\'
    #file_name = home_folder + '00001.vcf'

    # debug_object = ContactList(file_name)
    #debug_object = ContactList(home_folder+'Dohromady', is_dir=True)
    #debug_object.find_duplicates()