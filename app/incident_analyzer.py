incident = input("Describe the SAP incident:")

if "production" in incident.lower() and "down" in incident.lower():
  print("\nIncident Type: Production System Down.")
  print("Severity: Critical")

  print("\nPossible Causes:")
  print("- SAP application server stopped")
  print("- Database unavailable")
  print("- Operating system issue")
  print("- Network connectivity problem")

  print("\n Evidence required:")
  print("- SAP system status")
  print("- Database status")
  print("- SAP system logs")
  print("- Operating system status")

  print("\nFirst troubleshooting steps:")
  print("1. Check whether SAP application server is running.")
  print("2. Check database availability.")
  print("3. Check SAP system logs.")
  print("4. Check operating system resources.")
  print("5. Check network connectivity.")

else:
  print("\nIncident not recognized yet.")
  print("We will add more SAP scenerios later.")