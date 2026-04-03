import React, { useEffect, useState } from 'react';

const Users = () => {
  const [users, setUsers] = useState([]);
  const endpoint = `https://${process.env.REACT_APP_CODESPACE_NAME}-8000.app.github.dev/api/users/`;

  useEffect(() => {
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        const results = Array.isArray(data) ? data : data.results || [];
        setUsers(results);
        console.log('Users endpoint:', endpoint);
        console.log('Fetched users:', data);
      })
      .catch(err => console.error('Error fetching users:', err));
  }, [endpoint]);

  return (
    <div className="card shadow mb-4">
      <div className="card-header bg-secondary text-white">
        <h2 className="h4 mb-0">Users</h2>
      </div>
      <div className="card-body">
        <div className="table-responsive">
          <table className="table table-striped table-hover align-middle">
            <thead className="table-light">
              <tr>
                {users[0] && Object.keys(users[0]).map((key) => (
                  <th key={key}>{key}</th>
                ))}
              </tr>
            </thead>
            <tbody>
              {users.map((user, idx) => (
                <tr key={user.id || idx}>
                  {Object.values(user).map((val, i) => (
                    <td key={i}>{typeof val === 'object' ? JSON.stringify(val) : val}</td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
          {users.length === 0 && <div className="text-muted">No users found.</div>}
        </div>
      </div>
    </div>
  );
};

export default Users;
