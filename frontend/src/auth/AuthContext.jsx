/**
 * Authentication Context
 * Manages user authentication state using msalInstance directly
 */

import { createContext, useState, useCallback, useEffect, useContext } from 'react';
import { msalInstance } from './msalConfig';

export const AuthContext = createContext(null);

export function AuthProvider({ children }) {
  const [user, setUser] = useState(null);
  const [isLoading, setIsLoading] = useState(true);

  // Initialize user on mount
  useEffect(() => {
    const account = msalInstance.getActiveAccount();
    setUser(account);
    setIsLoading(false);
  }, []);

  const isAuthenticated = useCallback(() => {
    return user !== null;
  }, [user]);

  const getUserDisplayName = useCallback(() => {
    if (user && user.name) {
      return user.name;
    }
    return null;
  }, [user]);

  const getUserEmail = useCallback(() => {
    if (user && user.username) {
      return user.username;
    }
    return null;
  }, [user]);

  const value = {
    user,
    isAuthenticated: isAuthenticated(),
    isLoading,
    getUserDisplayName: getUserDisplayName(),
    getUserEmail: getUserEmail(),
  };

  return (
    <AuthContext.Provider value={value}>
      {children}
    </AuthContext.Provider>
  );
}

export function useAuth() {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within AuthProvider');
  }
  return context;
}
