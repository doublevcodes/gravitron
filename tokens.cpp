#include <iostream>
#include <string>
#include <map>
#include "tokens.hpp"

class VObject{
    public:
        // Attributes
        std::string __ref__;
        std::string __type__;
        int __mem_alloc__;
        VObject(std::string __ref__, std::string __type__, int __mem_alloc__) {

        }
};

class Int: public VObject{
    public:
        // Attributes
        std::string __ref__;
        int __base__;
        int __val__;
        Int() {
            VObject int_obj = new VObject()
        }
};