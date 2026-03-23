{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "7cce1edf-fc40-4a1b-b727-3676ac6076c7",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2026-03-24 01:05:48.287 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-24 01:05:48.289 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-24 01:05:49.353 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\Lenovo\\anaconda3\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n",
      "2026-03-24 01:05:49.354 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-24 01:05:49.356 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-24 01:05:49.357 No runtime found, using MemoryCacheStorageManager\n",
      "2026-03-24 01:05:49.361 No runtime found, using MemoryCacheStorageManager\n",
      "2026-03-24 01:05:49.363 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-24 01:05:49.365 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-24 01:05:49.367 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-24 01:05:49.370 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-24 01:05:49.412 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-24 01:05:49.414 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-24 01:05:49.415 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-24 01:05:49.417 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-24 01:05:49.419 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-24 01:05:49.421 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-24 01:05:49.425 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-24 01:05:49.427 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-24 01:05:49.430 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-24 01:05:49.432 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-24 01:05:49.434 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-24 01:05:49.436 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-24 01:05:49.437 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-24 01:05:49.439 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-24 01:05:49.441 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-24 01:05:49.482 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-24 01:05:49.483 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-24 01:05:49.485 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-24 01:05:49.486 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-24 01:05:49.486 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-24 01:05:49.487 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-24 01:05:49.493 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-24 01:05:49.495 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-24 01:05:49.496 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-24 01:05:49.497 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-24 01:05:49.498 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-24 01:05:49.499 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-24 01:05:49.501 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-24 01:05:49.502 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-24 01:05:49.504 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-24 01:05:49.509 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-24 01:05:49.511 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-24 01:05:49.515 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-24 01:05:49.517 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-24 01:05:49.520 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2026-03-24 01:05:49.520 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "\n",
    "st.set_page_config(page_title=\"AI Intraday Scanner\", layout=\"wide\")\n",
    "\n",
    "st.title(\"📈 AI Intraday Trading Dashboard\")\n",
    "\n",
    "# Load data\n",
    "@st.cache_data\n",
    "def load_data():\n",
    "    return pd.read_csv(\"results.csv\")\n",
    "\n",
    "try:\n",
    "    df = load_data()\n",
    "except:\n",
    "    st.error(\"Run scanner first in Jupyter!\")\n",
    "    st.stop()\n",
    "\n",
    "# Sidebar filter\n",
    "st.sidebar.header(\"Filters\")\n",
    "min_conf = st.sidebar.slider(\"Min Confidence\", 0.0, 1.0, 0.65)\n",
    "\n",
    "# All data\n",
    "st.subheader(\"📊 All Stocks\")\n",
    "st.dataframe(df)\n",
    "\n",
    "# Best trades\n",
    "st.subheader(\"🔥 Best Trades\")\n",
    "\n",
    "best = df[(df[\"signal\"] == \"BUY\") & (df[\"confidence\"] > min_conf)]\n",
    "st.dataframe(best)\n",
    "\n",
    "# Metrics\n",
    "st.subheader(\"📌 Summary\")\n",
    "st.metric(\"Total Stocks\", len(df))\n",
    "st.metric(\"BUY\", len(df[df[\"signal\"] == \"BUY\"]))\n",
    "st.metric(\"SELL\", len(df[df[\"signal\"] == \"SELL\"]))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d8b29482-c8b4-43f8-bf84-a762b0d1dfc9",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
