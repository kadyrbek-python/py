class bancAccauont:

    def __init__(self,name, balans):
        self._name = name
        self._balans = balans

    @property
    def name(self):
        return f"my Accauont:{self._name}"
    @property
    def balans(self):
        if self._balans < 0:
            print(None)
        else:
            return f"my balans:{self._balans}"

Accauont = bancAccauont('kadyrbek', 2000)
Accauont._balans = -300

print(Accauont.name)
print(Accauont.balans)
