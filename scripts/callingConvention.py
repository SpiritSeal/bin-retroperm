import angr

p = angr.Project('../executables/fauxware', auto_load_libs=False)

# Determine the function calling convention of the binary
print("Calling convention: ", p.arch.calling_convention)