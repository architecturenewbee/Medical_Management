cmake_minimum_required(VERSION 3.23.0)
project(MedClass)
add_library(MedClass MedCLass.cpp)
target_include_directories(MedClass PUBLIC ./include)