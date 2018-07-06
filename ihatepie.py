import gdb
class br(gdb.Command):
    __base_addr=0
    __libc_base_addr=0

    def __init__(self):
	    super(self.__class__, self).__init__("br", gdb.COMMAND_USER)

    def __readfile(self,filename):
        f = open(filename)
        r=f.readlines()
        f.close()
        return r 
    def __readf(self,filename):
        f = open(filename,'rb')
        r=f.read()
        f.close()
        return r 
    def __exe(self):
        for obj in gdb.objfiles():
            if obj.filename:
                return obj.filename
            break

    def __getaddr(self,isl):
        pid=gdb.execute('pid', to_string=True)
        pid=pid[0:-1]
        locations = [
        '/proc/%s/maps' % pid,
        '/proc/%s/map'  % pid,
        '/usr/compat/linux/proc/%s/maps'  % pid,
        ]

        for location in locations:
            try:
                data = self.__readfile(location)
                break
            except (OSError, gdb.error):
                continue
        exe=self.__exe()
        if(isl=='l'):
            for addr in data:
                if(addr.find('libc')!=-1):
                    self.__libc_base_addr=int('0x'+addr.split('-')[0],16) 
                    break

        else:

            for addr in data:
                if(addr.find(exe)!=-1):
                    self.__base_addr=int('0x'+addr.split('-')[0],16) 
                    break

  
    def invoke(self, args, from_tty):
        argv = gdb.string_to_argv(args)
        if len(argv) < 1:
            raise gdb.GdbError('param error')
        if (argv[0]!='l'):
            exe=self.__exe()
            data=self.__readf(exe)
            if(data[17]==0x2):
                gdb.execute('b *'+args)
                return      
    
        self.__getaddr(argv[0])
        try:

            if(argv[0]=='l'):
                s='b *'+str(hex(int(argv[1],16)+self.__libc_base_addr))
            else:
                s='b *'+str(hex(int(argv[0],16)+self.__base_addr))

        except:
            raise gdb.GdbError('error to find addr')
            return
        if (len(argv) >2 and argv[0]=='l'):
            for argc in argv[2:]:
                s+=' '+argc
        if (len(argv) >1 and argv[0]!='l'):
            for argc in argv[1:]:
                s+=' '+argc

        gdb.execute(s)     
        
br()
