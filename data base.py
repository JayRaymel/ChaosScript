import streamlit as st
from supabase import create_client, Client

#Configurar supabase
SUPABASE_URL = https://kayglsldzntqgagbqdui.supabase.co
SUPABASE_KEY = eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImtheWdsc2xkem50cWdhZ2JxZHVpIiwicm9sZSI6ImFub24iLCJpYXQiOjE3MjI0NzMzNDAsImV4cCI6MjAzODA0OTM0MH0.gX2JYbXV2PnYaAI36XKfOzCJw6zAjSRlPKAowp5v6ic
supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)