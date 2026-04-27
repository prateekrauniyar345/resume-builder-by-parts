/**
 * Microsoft Authentication Library (MSAL) Configuration for React
 * Configures OAuth 2.0 with Microsoft Entra ID for client-side authentication
 */

import { PublicClientApplication } from '@azure/msal-browser';

/**
 * MSAL Configuration Object
 * Update these with your Azure AD app registration details
 * Get these from: https://portal.azure.com -> App registrations
 */
const msalConfig = {
  auth: {
    // Azure AD App Registration - Application (client) ID
    clientId: import.meta.env.VITE_AZURE_CLIENT_ID || 'YOUR_AZURE_CLIENT_ID',
    
    // Azure AD Tenant ID or 'common' for multi-tenant
    authority: `https://login.microsoftonline.com/${
      import.meta.env.VITE_AZURE_TENANT_ID || 'common'
    }`,
    
    // Redirect URI - Must be registered in Azure AD app
    redirectUri: import.meta.env.VITE_AZURE_REDIRECT_URI || 'http://localhost:5173',
    
    // Post Logout Redirect - Where to send user after logout
    postLogoutRedirectUri: import.meta.env.VITE_AZURE_POST_LOGOUT_URI || 'http://localhost:5173',
  },
  cache: {
    cacheLocation: 'sessionStorage', // or 'localStorage'
    storeAuthStateInCookie: false,
  },
  system: {
    loggerOptions: {
      loggerCallback: (level, message, containsPii) => {
        if (containsPii) {
          return;
        }
        // Optional: Uncomment to see MSAL logs in console
        // console.log(level, message);
      },
    },
  },
};

/**
 * Scopes for API requests
 * Define what permissions the app needs
 */
export const apiScopes = {
  default: ['User.Read'],
  mail: ['Mail.Read'],
  calendar: ['Calendar.Read'],
};

/**
 * Login request configuration
 */
export const loginRequest = {
  scopes: apiScopes.default,
};

/**
 * Token request configuration for acquiring tokens
 */
export const tokenRequest = {
  scopes: apiScopes.default,
};

/**
 * Initialize and export MSAL Public Client Application
 */
export const msalInstance = new PublicClientApplication(msalConfig);

export default msalConfig;
