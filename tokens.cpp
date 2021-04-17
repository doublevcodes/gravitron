#include <iostream>
#include <string>
#include <map>
#include "tokens.hpp"

class VObject{
    public:
        // Attributes
        std::string __ref__;
        std::string __type__;
        auto __val__;
        int __mem_alloc__;
        VObject(std::string __ref__, std::string __type__, auto __val__, int __mem_alloc__) {

        }
};

class Int: public VObject{
    public:
        // Attributes
        std::string __ref__;
        int __base__ = 10;
        int __val__;
        Int(std::string __ref__, int __base__, int __val__) {
            VObject int_obj = new VObject(__ref__, __base__, __val__)
        }
};