
/* Capsule objects let you wrap a C "void *" pointer in a Python
   object.  They're a way of passing data through the Python interpreter
   without creating your own custom type.

   Capsules are used for communication between extension modules.
   They provide a way for an extension module to export a C interface
   to other extension modules, so that extension modules can use the
   Python import mechanism to link to one another.

   For more information, please see "c-api/capsule.html" in the
   documentation.
*/

#ifndef Py_CAPSULE_H
#define Py_CAPSULE_H
#ifdef __cplusplus
extern "C" {
#endif

#include "cpyext_capsule.h"

#define PyCapsule_CheckExact(op) (Py_TYPE(op) == &PyCapsule_Type)

PyAPI_FUNC(void *) PyCapsule_GetPointer(PyObject *capsule, const char *name);

PyAPI_FUNC(PyCapsule_Destructor) PyCapsule_GetDestructor(PyObject *capsule);

PyAPI_FUNC(const char *) PyCapsule_GetName(PyObject *capsule);

PyAPI_FUNC(void *) PyCapsule_GetContext(PyObject *capsule);

PyAPI_FUNC(int) PyCapsule_IsValid(PyObject *capsule, const char *name);

PyAPI_FUNC(void *) PyCapsule_Import(const char *name, int no_block);

PyAPI_FUNC(PyTypeObject *) _Py_get_capsule_type(void);

#ifdef __cplusplus
}
#endif
#endif /* !Py_CAPSULE_H */
