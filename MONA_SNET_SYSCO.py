# class MONA_SNET_SYSCO:
#     def Alerts(self):
#         print("monitoring status")

# class MONA:
#     def show_MONA(self):
#         print("monitoring MONA status")

# class SNET:
#     def show_SNET(self):
#         print("monitoring SNET status")

# class SYSCO:
#     def show_SYSCO(self):
#         print("monitoring SYSCO status")

# class status:               #this class is the real composed class in the code
#     def __init__(self):
#         self.mona=MONA()
#         self.snet=SNET()
#         self.sysco=SYSCO()

#     def Alerts(self):
#         self.mona.show_MONA()
#         self.snet.show_SNET()
#         self.sysco.show_SYSCO()

# mona_snet_sysco=status()
# mona_snet_sysco.Alerts()





# class MONA:
#     def show_MONA(self):
#         print("monitoring MONA status")

# class SNET:
#     def show_SNET(self):
#         print("monitoring SNET status")

# class SYSCO:
#     def show_SYSCO(self):
#         print("monitoring SYSCO status")

# class status:               #this class is the real composed class in the code
#     def __init__(self):
#         self.mona=MONA()
#         self.snet=SNET()
#         self.sysco=SYSCO()

#     def Alerts(self):
#         self.mona.show_MONA()
#         self.snet.show_SNET()
#         self.sysco.show_SYSCO()

# mona_snet_sysco=status()
# mona_snet_sysco.Alerts()




# class MONA_SNET_SYSCO:
#     def show_all(self):
#         print("monitoring all")

# class MONA:
#     def show_MONA(self):
#         print("monitoring MONA status")

# class SNET:
#     def show_SNET(self):
#         print("monitoring SNET status")

# class SYSCO:
#     def show_SYSCO(self):
#         print("monitoring SYSCO status")

# class status:               #this class is the real composed class in the code
#     def __init__(self):
#         self.mona_snet_sysco=MONA_SNET_SYSCO()
#         self.mona=MONA()
#         self.snet=SNET()
#         self.sysco=SYSCO()

#     def Alerts(self):
#         self.mona_snet_sysco.show_all()
#         self.mona.show_MONA()
#         self.snet.show_SNET()
#         self.sysco.show_SYSCO()

# mona_snet_sysco=status()
# mona_snet_sysco.Alerts()





class MONA_SNET_SYSCO:
    def show_all(self):
        print("monitoring all")

class MONA:
    def show_MONA(self):
        print("monitoring MONA status")

class SNET:
    def show_SNET(self):
        print("monitoring SNET status")

class SYSCO:
    def show_SYSCO(self):
        print("monitoring SYSCO status")

class status:               #this class is the real composed class in the code
    def __init__(self):
        self.mona_snet_sysco=MONA_SNET_SYSCO()
        self.mona=MONA()
        self.snet=SNET()
        self.sysco=SYSCO()

    def Alerts(self):
        self.mona_snet_sysco.show_all()
        self.mona.show_MONA()
        self.snet.show_SNET()
        self.sysco.show_SYSCO()

x=status()
x.Alerts()