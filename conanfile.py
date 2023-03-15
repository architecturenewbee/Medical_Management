from conans import ConanFile, CMake

class Medical(ConanFile):
    name= "Medical_Management"
    version="1.0"
    description= "This is a inventory management tool"
    settings = {"arch":None, "os":None, "build_type":None, "compiler":None}

    def build(self):
        cmake = CMake(self)
        cmake.configure()        
        cmake.build()
