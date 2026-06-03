from fastapi import FastAPI, HTTPException
from schemas import Employee, EmployeeUpdate

app = FastAPI()

employees = []

# CREATE
@app.post("/employees")
def create_employee(employee: Employee):

    employee_data = employee.model_dump()

    employee_data["id"] = len(employees) + 1

    employees.append(employee_data)

    return {
        "message": "Employee created",
        "data": employee_data
    }


# READ ALL
@app.get("/employees")
def get_employees():

    return employees


# READ ONE
@app.get("/employees/{employee_id}")
def get_employee(employee_id: int):

    for emp in employees:
        if emp["id"] == employee_id:
            return emp

    raise HTTPException(
        status_code=404,
        detail="Employee not found"
    )


# UPDATE
@app.put("/employees/{employee_id}")
def update_employee(
    employee_id: int,
    updated: EmployeeUpdate
):

    for emp in employees:

        if emp["id"] == employee_id:

            update_data = updated.model_dump(
                exclude_unset=True
            )

            emp.update(update_data)

            return {
                "message": "Updated",
                "data": emp
            }

    raise HTTPException(
        status_code=404,
        detail="Employee not found"
    )


# DELETE
@app.delete("/employees/{employee_id}")
def delete_employee(employee_id: int):

    for index, emp in enumerate(employees):

        if emp["id"] == employee_id:

            removed = employees.pop(index)

            return {
                "message": "Deleted",
                "data": removed
            }

    raise HTTPException(
        status_code=404,
        detail="Employee not found"
    )