cmake_minimum_required(VERSION 3.12)

# Set the project name
project(pynum LANGUAGES CXX)

find_package(Python3 COMPONENTS Interpreter Development REQUIRED)
find_package(pybind11 REQUIRED)

set(MODULE_NAME dtypes)

set(SRC_FILE pynum/src/dtypes.cpp)

pybind11_add_module(${MODULE_NAME} ${SRC_FILE})

target_include_directories(${MODULE_NAME} PRIVATE ${Python3_INCLUDE_DIRS})

