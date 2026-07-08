import { useMutation, useQuery, useQueryClient } from '@tanstack/react-query'
import { type FormEvent, useEffect, useState } from 'react'
import './App.css'

type Employee = {
  emp_id: number
  emp_name: string
  designation: string | null
  created_at: string | null
  updated_at: string | null
}

type EmployeePayload = {
  emp_name: string
  designation: string
}

async function fetchEmployees(): Promise<Employee[]> {
  const response = await fetch('http://127.0.0.1:8000/employees')
  if (!response.ok) {
    throw new Error('Failed to fetch employees')
  }
  return response.json()
}

async function createEmployee(payload: EmployeePayload): Promise<Employee> {
  const response = await fetch('http://127.0.0.1:8000/employees', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload),
  })

  if (!response.ok) {
    throw new Error('Failed to create employee')
  }

  return response.json()
}

function App() {
  const queryClient = useQueryClient()
  const [formData, setFormData] = useState<EmployeePayload>({ emp_name: '', designation: '' })

  const { data, isLoading, error } = useQuery({
    queryKey: ['employees'],
    queryFn: fetchEmployees,
  })

  const mutation = useMutation({
    mutationFn: createEmployee,
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['employees'] })
      setFormData({ emp_name: '', designation: '' })
    },
  })

  function handleSubmit(event: FormEvent<HTMLFormElement>) {
    event.preventDefault()
    mutation.mutate(formData)
  }

  return (
    <div className="min-h-screen bg-slate-100 px-6 py-10 text-slate-800">
      <div className="mx-auto max-w-6xl rounded-2xl bg-white p-8 shadow-lg">

        <div className="mb-6">
          <p className="text-sm font-semibold uppercase tracking-[0.3em] text-blue-600">
            Employee Directory
          </p>
          <h1 className="mt-2 text-3xl font-bold">Employee records</h1>
          <p className="mt-2 text-sm text-slate-500">
            Add a new employee and view the latest list from the FastAPI backend.
          </p>
        </div>

        <div className="grid gap-6 lg:grid-cols-[1.3fr_0.7fr]">
          <div>
            {isLoading && <p className="text-sm text-slate-500">Loading employees...</p>}
            {error && <p className="text-sm text-red-600">{error.message}</p>}

            {!isLoading && !error && (
              <div className="overflow-hidden rounded-xl border border-slate-200">
                <table className="min-w-full divide-y divide-slate-200">
                  <thead className="bg-slate-50">
                    <tr>
                      <th className="px-4 py-3 text-left text-sm font-semibold">ID</th>
                      <th className="px-4 py-3 text-left text-sm font-semibold">Name</th>
                      <th className="px-4 py-3 text-left text-sm font-semibold">Designation</th>
                      <th className="px-4 py-3 text-left text-sm font-semibold">Created</th>
                    </tr>
                  </thead>
                  <tbody className="divide-y divide-slate-200 bg-white">
                    {data?.map((employee) => (
                      <tr key={employee.emp_id} className="hover:bg-slate-50">
                        <td className="px-4 py-3 text-sm">{employee.emp_id}</td>
                        <td className="px-4 py-3 text-sm font-medium">{employee.emp_name}</td>
                        <td className="px-4 py-3 text-sm">{employee.designation ?? '—'}</td>
                        <td className="px-4 py-3 text-sm">{employee.created_at ? new Date(employee.created_at).toLocaleString() : '—'}</td>
                      </tr>
                    ))}
                  </tbody>
                </table>
              </div>
            )}
          </div>

          <form onSubmit={handleSubmit} className="rounded-2xl border border-slate-200 bg-slate-50 p-6 shadow-sm">
            <h2 className="text-xl font-semibold text-slate-800">Add employee</h2>
            <p className="mt-1 text-sm text-slate-500">Create a new employee record.</p>

            <div className="mt-4 space-y-4">
              <div>
                <label className="mb-1 block text-sm font-medium text-slate-700">Employee name</label>
                <input
                  required
                  value={formData.emp_name}
                  onChange={(event) => setFormData({ ...formData, emp_name: event.target.value })}
                  className="w-full rounded-lg border border-slate-300 px-3 py-2 focus:border-blue-500 focus:outline-none"
                  placeholder="Enter full name"
                />
              </div>

              <div>
                <label className="mb-1 block text-sm font-medium text-slate-700">Designation</label>
                <input
                  value={formData.designation}
                  onChange={(event) => setFormData({ ...formData, designation: event.target.value })}
                  className="w-full rounded-lg border border-slate-300 px-3 py-2 focus:border-blue-500 focus:outline-none"
                  placeholder="Enter designation"
                />
              </div>
            </div>

            <button
              type="submit"
              disabled={mutation.isPending}
              className="mt-6 w-full rounded-lg bg-blue-600 px-4 py-2 font-medium text-white transition hover:bg-blue-700 disabled:cursor-not-allowed disabled:bg-blue-400"
            >
              {mutation.isPending ? 'Creating...' : 'Add employee'}
            </button>

            {mutation.isError && <p className="mt-3 text-sm text-red-600">Unable to create employee.</p>}
            {mutation.isSuccess && <p className="mt-3 text-sm text-green-600">Employee added successfully.</p>}
          </form>
        </div>
      </div>
    </div>
  )
}

export default App
