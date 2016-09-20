from acitoolkit.acitoolkit import *
"""
"""
def main(login,password,url):

	print "Enter Tenant"
	tenant_var = raw_input(" >>  ")

	# Create the Tenant
	tenant = Tenant(tenant_var)

	print "Enter Application Name"
	app_var = raw_input(" >>  ")

	# Create the Application Profile
	app = AppProfile(app_var, tenant)

	print "Enter EPG Name"
	epg_var = raw_input(" >>  ")

	# Create the EPG
	epg = EPG(epg_var, app)

	print "Enter Context Name"
	context_var = raw_input(" >>  ")

	print "Enter Bridge Name"
	bridge_var = raw_input(" >>  ")

	# Create a Context and BridgeDomain
	context = Context(context_var, tenant)
	bd = BridgeDomain(bridge_var, tenant)
	bd.add_context(context)

	# Place the EPG in the BD
	epg.add_bd(bd)


	# Declare 2 physical interfaces
	if1 = Interface('eth', '1', '101', '1', '3')
	if2 = Interface('eth', '1', '102', '1', '3')

	# Create VLAN 5 on the physical interfaces
	vlan1098_on_if1 = L2Interface('vlan1098_on_if1', 'vlan', '1098')
	vlan1098_on_if1.attach(if1)

	vlan1098_on_if2 = L2Interface('vlan1098_on_if2', 'vlan', '1098')
	vlan1098_on_if2.attach(if2)

	# Attach the EPG to the VLANs
	epg.attach(vlan1098_on_if1)
	epg.attach(vlan1098_on_if2)

	# Get the APIC login credentials
	#creds = Credentials('apic', description)
	#args = creds.get()

	# Login to APIC and push the config
	#session = Session(args.url, args.login, args.password)
	session = Session(url, login, password)
	session.login()
	resp = tenant.push_to_apic(session)
	if resp.ok:
		print 'Success'


	# Print what was sent
	#print 'Pushed the following JSON to the APIC'
	#print 'URL:', tenant.get_url()
	#print 'JSON:', tenant.get_json()

if __name__ == '__main__':
	main()
