from conans import ConanFile, CMake

class CapiCoreConan(ConanFile):
   settings = "os", "compiler", "build_type", "arch"
   requires = ""
   generators = "cmake", "gcc", "txt"
   default_options = {-DCMAKE_INSTALL_PREFIX=/usr/local }

   def imports(self):
      pass

   def build(self):
      cmake = CMake(self)
      cmake.configure()
      cmake.build()
