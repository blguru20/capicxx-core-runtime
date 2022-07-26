from conans import ConanFile, CMake

class CapiCoreConan(ConanFile):
   settings = "os", "compiler", "build_type", "arch"
   generators = "cmake", "gcc", "txt"

   def configure_cmake(self): 
      cmake = CMake(self)
      cmake.definitions['CMAKE_INSTALL_PREFIX'] = '_artifacts'

   def imports(self):
      pass

   def build(self):
      cmake = CMake(self)
      cmake.configure()
      cmake.build()
      
   def package(self):
      cmake = CMake(self)
      cmake.install()
