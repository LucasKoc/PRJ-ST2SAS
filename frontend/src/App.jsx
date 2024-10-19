import React, {useEffect, useState} from 'react';
import {Tab, TabList, TabPanel, Tabs} from 'react-tabs';
import 'react-tabs/style/react-tabs.css';
import 'tailwindcss/tailwind.css';

const API_URL = 'http://localhost:3000';

const DataList = ({endpoint, title, columns, refresh}) => {
    const [data, setData] = useState([]);
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        setLoading(true);
        fetch(`${API_URL}${endpoint}`)
            .then((response) => response.json())
            .then((data) => {
                setData(data);
                setLoading(false);
            })
            .catch((error) => console.error('Error fetching data:', error));
    }, [endpoint, refresh]);

    if (loading) {
        return <p className="text-center text-lg">Loading {title}...</p>;
    }

    return (<div>
        <h3 className="text-xl font-semibold mb-4">{title}</h3>
        <div className="overflow-x-auto">
            <table className="table table-zebra w-full">
                <thead>
                <tr>
                    {columns.map((col, index) => (<th key={index}>{col.header}</th>))}
                </tr>
                </thead>
                <tbody>
                {data.map((item, index) => (<tr key={index}>
                    {columns.map((col, colIndex) => (<td key={colIndex}>{item[col.accessor]}</td>))}
                </tr>))}
                </tbody>
            </table>
        </div>
    </div>);
};

const AddDataForm = ({endpoint, fields, initialState, onSuccess}) => {
    const [formData, setFormData] = useState(initialState);
    const [error, setError] = useState(null);
    const [formErrors, setFormErrors] = useState({});

    const handleChange = (e) => {
        const {name, value} = e.target;
        setFormData((prevData) => ({...prevData, [name]: value}));
    };

    const validate = () => {
        const errors = {};
        fields.forEach((field) => {
            if (field.required && !formData[field.name]) {
                errors[field.name] = `${field.label} is required`;
            }
        });
        return errors;
    };

    const handleSubmit = (e) => {
        e.preventDefault();

        // Perform validation
        const errors = validate();
        if (Object.keys(errors).length > 0) {
            setFormErrors(errors);
            return;
        }

        // Create a copy of formData but only include non-empty values
        const filteredData = Object.fromEntries(
            Object.entries(formData).filter(([key, value]) => value !== '' && value !== null && value !== undefined)
        );

        fetch(`${API_URL}${endpoint}`, {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(filteredData), // Only send non-empty fields
        })
            .then((response) => {
                if (!response.ok) {
                    return response.json().then((errorDetails) => {
                        throw new Error(errorDetails.detail || 'Failed to submit data');
                    });
                }
                return response.json();
            })
            .then((data) => {
                console.log('Post request:', data);
                setFormData(initialState);
                setError(null);
                setFormErrors({});
                onSuccess();
            })
            .catch((error) => {
                setError(error.message);
                console.error('Error adding data:', error);
            });
    };

    return (
        <form onSubmit={handleSubmit} className="space-y-6 bg-white p-6 rounded-lg shadow-lg">
            {fields.map((field, index) => (
                <div key={index} className="form-control">
                    <label className="label">
                        <span className="label-text font-semibold">{field.label}</span>
                    </label>
                    <input
                        type={field.type}
                        name={field.name}
                        value={formData[field.name]}
                        onChange={handleChange}
                        placeholder={field.placeholder}
                        className="input input-bordered w-full max-w-md"
                    />
                    {formErrors[field.name] && (
                        <p className="text-red-500 text-sm">{formErrors[field.name]}</p>
                    )}
                </div>
            ))}
            {error && <p className="text-red-500">{error}</p>}
            <button type="submit" className="btn btn-primary btn-block">
                Add
            </button>
        </form>
    );
};


const App = () => {
    const [refreshStudents, setRefreshStudents] = useState(0);
    const [refreshTeachers, setRefreshTeachers] = useState(0);
    const [refreshCourses, setRefreshCourses] = useState(0);
    const [refreshEnrollments, setRefreshEnrollments] = useState(0);

    const studentColumns = [{header: "Student ID", accessor: "student_id"}, {
        header: "First Name",
        accessor: "first_name"
    }, {header: "Last Name", accessor: "last_name"}, {header: "Email", accessor: "school_email"}, {
        header: "Phone",
        accessor: "phone"
    },];

    const teacherColumns = [{header: "Teacher ID", accessor: "teacher_id"}, {
        header: "First Name",
        accessor: "first_name"
    }, {header: "Last Name", accessor: "last_name"}, {header: "Email", accessor: "school_email"}, {
        header: "Phone",
        accessor: "phone"
    }, {header: "Speciality", accessor: "speciality"},];

    const courseColumns = [{header: "Course ID", accessor: "course_id"}, {
        header: "Course Name",
        accessor: "course_name"
    }, {header: "Teacher ID", accessor: "teacher_id"},];

    const enrollmentColumns = [{header: "Student ID", accessor: "student_id"}, {
        header: "Course ID",
        accessor: "course_id"
    }, {header: "Grade", accessor: "grade"},];

    // Fields for forms
    const studentFields = [{
        label: "Student ID",
        name: "student_id",
        type: "number",
        placeholder: "Enter student ID",
        required: true
    }, {label: "First Name", name: "first_name", type: "text", placeholder: "Enter first name", required: true}, {
        label: "Last Name",
        name: "last_name",
        type: "text",
        placeholder: "Enter last name",
        required: true
    }, {label: "Email", name: "school_email", type: "email", placeholder: "Enter email", required: true}, {
        label: "Phone",
        name: "phone",
        type: "text",
        placeholder: "Enter phone number"
    },];

    const teacherFields = [{
        label: "Teacher ID",
        name: "teacher_id",
        type: "text",
        placeholder: "Enter teacher ID",
        required: true
    }, {label: "First Name", name: "first_name", type: "text", placeholder: "Enter first name", required: true}, {
        label: "Last Name",
        name: "last_name",
        type: "text",
        placeholder: "Enter last name",
        required: true
    }, {label: "Email", name: "school_email", type: "email", placeholder: "Enter email", required: true}, {
        label: "Phone",
        name: "phone",
        type: "text",
        placeholder: "Enter phone number"
    }, {label: "Speciality", name: "speciality", type: "text", placeholder: "Enter speciality", required: true},];

    const courseFields = [{
        label: "Course ID",
        name: "course_id",
        type: "text",
        placeholder: "Enter course ID",
        required: true
    }, {
        label: "Course Name",
        name: "course_name",
        type: "text",
        placeholder: "Enter course name",
        required: true
    }, {label: "Teacher ID", name: "teacher_id", type: "text", placeholder: "Enter teacher ID", required: true},];

    const enrollmentFields = [{
        label: "Student ID",
        name: "student_id",
        type: "number",
        placeholder: "Enter student ID",
        required: true
    }, {label: "Course ID", name: "course_id", type: "text", placeholder: "Enter course ID", required: true}, {
        label: "Grade",
        name: "grade",
        type: "number",
        placeholder: "Enter grade"
    },];

    return (<div className="p-4">
        <h1 className="text-3xl font-bold text-center mb-8">School Manager</h1>

        <Tabs>
            <TabList className="tabs mb-6">
                <Tab className="tab tab-lifted">Students</Tab>
                <Tab className="tab tab-lifted">Teachers</Tab>
                <Tab className="tab tab-lifted">Courses</Tab>
                <Tab className="tab tab-lifted">Enrollments</Tab>
            </TabList>

            <TabPanel>
                <DataList endpoint="/students" title="Students List" columns={studentColumns}
                          refresh={refreshStudents}/>
                <AddDataForm
                    endpoint="/students"
                    fields={studentFields}
                    initialState={{student_id: '', first_name: '', last_name: '', school_email: '', phone: ''}}
                    onSuccess={() => setRefreshStudents((prev) => prev + 1)}
                />
            </TabPanel>

            <TabPanel>
                <DataList endpoint="/teachers" title="Teachers List" columns={teacherColumns}
                          refresh={refreshTeachers}/>
                <AddDataForm
                    endpoint="/teachers"
                    fields={teacherFields}
                    initialState={{
                        teacher_id: '', first_name: '', last_name: '', school_email: '', phone: '', speciality: ''
                    }}
                    onSuccess={() => setRefreshTeachers((prev) => prev + 1)}
                />
            </TabPanel>

            <TabPanel>
                <DataList endpoint="/courses" title="Courses List" columns={courseColumns}
                          refresh={refreshCourses}/>
                <AddDataForm
                    endpoint="/courses"
                    fields={courseFields}
                    initialState={{course_id: '', course_name: '', teacher_id: ''}}
                    onSuccess={() => setRefreshCourses((prev) => prev + 1)}
                />
            </TabPanel>

            <TabPanel>
                <DataList endpoint="/enrollments" title="Enrollments List" columns={enrollmentColumns}
                          refresh={refreshEnrollments}/>
                <AddDataForm
                    endpoint="/enrollments"
                    fields={enrollmentFields}
                    initialState={{student_id: '', course_id: '', grade: '0'}}
                    onSuccess={() => setRefreshEnrollments((prev) => prev + 1)}
                />
            </TabPanel>
        </Tabs>
    </div>);
};

export default App;
