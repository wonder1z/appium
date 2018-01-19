from PageObject import Pages


class ManyHistoryPage:
    '''
    多次浏览微社区历史
    '''

    def __init__(self, kwargs):
        _init = {"driver": kwargs["driver"], "path": kwargs["path"], "device": kwargs["device"],
                 "logTest": kwargs["logTest"], "caseName": kwargs["caseName"]}
        self.page = Pages.PagesObjects(_init)

        '''
        操作步骤
        '''

    def operate(self):
        self.page.operate()

    def checkPoint(self):
        _check = {"check": "contrary_getval"}
        self.page.checkPoint(_check)

if __name__ == "__main__":
    pass
