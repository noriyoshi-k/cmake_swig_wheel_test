%module test
%{
#define SWIG_FILE_WITH_INIT
#include "test.hpp"
%}

#if defined(SWIGPYTHON)
%include "numpy.i"
#endif
#if defined(SWIGPYTHON)
%init %{
    import_array();
    %}
%apply (short* IN_ARRAY1, int DIM1) {(short* buf,int n)};
%apply (float* IN_ARRAY1, int DIM1) {(float* buf, int size)};
#endif

%include "test.hpp"