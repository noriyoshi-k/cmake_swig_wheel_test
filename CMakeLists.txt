CMAKE_MINIMUM_REQUIRED(VERSION 2.4)
project(test)

if(${CMAKE_SYSTEM_NAME} MATCHES "Darwin")
    set(CMAKE_CXX_FLAGS "-std=c++11 -stdlib=libc++")
elseif(${CMAKE_SYSTEM_NAME} MATCHES "Linux")
    set(CMAKE_CXX_FLAGS "-std=c++11")
endif()

find_package(PythonLibs REQUIRED)
find_package(SWIG REQUIRED)
include (UseSWIG)

include(FindNumPy.cmake)
include(${SWIG_USE_FILE})
include(GenerateExportHeader)

include_directories(
    ${CMAKE_CURRENT_SOURCE_DIR}
    ${PROJECT_BINARY_DIR}
    ${PYTHON_INCLUDE_PATH}
    ${PYTHON_NUMPY_INCLUDE_DIR}
)

set(INTERFACE_FILES
    test.i
)

set_source_files_properties(${INTERFACE_FILES} PROPERTIES CPLUSPLUS ON)

swig_add_module(test python ${INTERFACE_FILES}
    test.cpp
    test.hpp
)

swig_link_libraries(test
    ${PYTHON_LIBRARIES}
)
